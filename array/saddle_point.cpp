#include <iostream>
#include <climits>
using namespace std;

void display(int **arr, int n, int m)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cout << arr[i][j] << " ";
        }
        cout << endl;
    }
}

void saddlePoint(int row, int col, int **arr)
{
    for (int i = 0; i < row; i++)
    {
        // Find the minimum element in the row
        int minVal = arr[i][0];
        int minCol = 0;
        for (int j = 1; j < col; j++)
        {
            if (arr[i][j] < minVal)
            {
                minVal = arr[i][j];
                minCol = j;
            }
        }

        // Check if this minimum is the maximum in its column
        bool isSaddle = true;
        for (int k = 0; k < row; k++)
        {
            if (arr[k][minCol] > minVal)
            {
                isSaddle = false;
                break;
            }
        }

        if (isSaddle)
        {
            cout << "Saddle point found: " << minVal << " at (" << i << ", " << minCol << ")" << endl;
            return;
        }
    }
    cout << "No saddle point found." << endl;
}

int main()
{
    int row = 3, col = 3;
    int **arr = new int *[row];
    arr[0] = new int[col]{1, 2, 3};
    arr[1] = new int[col]{4, 5, 6};
    arr[2] = new int[col]{7, 8, 9};

    cout << "Matrix:" << endl;
    display(arr, row, col);

    saddlePoint(row, col, arr);

    // Deallocate memory
    for (int i = 0; i < row; i++)
    {
        delete[] arr[i];
    }
    delete[] arr;

    return 0;
}
