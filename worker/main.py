from worker.task_worker import TaskWorker


def main():
    worker = TaskWorker()
    worker.start()


if __name__ == "__main__":
    main()
