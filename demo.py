import numpy as np
import pickle


def main():
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)

    example_data = np.array([
        [35.77, 10.],
        [150.9, 20.],
        [70.086, 5.]
    ])

    result = model.predict_proba(example_data)[:, 1]
    for r in result:
        print(r)


if __name__ == "__main__":
    main()
