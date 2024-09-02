
import numpy as np
import pandas as pd

a = np.array([2,3,4])
b = np.array([1.2,3.5,5.1])
c =  np.array([[1,2],[3,4]], dtype=complex)

d = np.zeros((2,4))
e = np.ones((2,9))
f = np.empty((2,5))


df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)

print(df)