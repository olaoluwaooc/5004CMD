from dask.distributed import Client
import time
import pandas as pd


# the funcs
def question1(big_dataset, small_dataset):
    weekly_home = small_dataset.groupby(
        small_dataset['Date'].dt.isocalendar().week
    )['Population Staying at Home'].mean()
    return weekly_home


def question2(big_dataset):
    national = big_dataset[big_dataset['Level'] == "National"]
    col_10_25 = [col for col in national.columns if "10-25" in col][0]
    return national[national[col_10_25] > 10000000]


def question3(big_dataset):
    national = big_dataset[big_dataset['Level'] == "National"]
    col_10_25 = [col for col in national.columns if "10-25" in col][0]
    col_50_100 = [col for col in national.columns if "50-100" in col][0]
    return national[[col_10_25, col_50_100]]


def question4(big_dataset):
    national = big_dataset[big_dataset['Level'] == "National"]
    distance_cols = [col for col in national.columns if "Trips" in col]
    return national[distance_cols].mean()



# execution
if __name__ == "__main__":

    # datasets
    small_dataset = pd.read_csv("Trips_by_Distance.csv", parse_dates=['Date'])
    big_dataset = pd.read_csv("Trips_Full Data.csv", parse_dates=['Date'])

    small_dataset.columns = small_dataset.columns.str.strip()
    big_dataset.columns = big_dataset.columns.str.strip()


    # sequential
    start_seq = time.time()

    question1(big_dataset, small_dataset)
    question2(big_dataset)
    question3(big_dataset)
    question4(big_dataset)

    seq_time = time.time() - start_seq
    print("Sequential Time:", seq_time)


    # parallel
    n_processors = [10, 20]
    execution_times = {}

    for n in n_processors:
        print(f"\nRunning with {n} workers...")

        client = Client(n_workers=n)

        start = time.time()

        question1(big_dataset, small_dataset)
        question2(big_dataset)
        question3(big_dataset)
        question4(big_dataset)

        elapsed = time.time() - start
        execution_times[n] = elapsed

        print(f"Time with {n} workers:", elapsed)

        client.close()


    # output
    print("\nCOMPARISON")
    print("Sequential:", seq_time)

    for k, v in execution_times.items():
        print(f"{k} workers:", v)