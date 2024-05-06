#include <iostream>

using namespace std;

int main() 
{
	int num1,num2,num3;
	
	while (true) {
		cin >> num1 >> num2 >> num3;
		if (num1 == 0 and num2 == 0 and num3 == 0) {
			return 0;
		}
		int arr[3] = {num1,num2,num3};
		int max_idx = 0;
		int max_v = arr[0];
		for (int i = 0; i < 3; i++)
		{
			if (max_v < arr[i]) 
			{
				max_v = arr[i];
				max_idx = i;
			}
		}
		int other1 = 0;
		int other2 = 0;
		if (max_idx == 0)
		{
			other1 = arr[1];
			other2 = arr[2];
		}
		else if (max_idx == 1)
		{
			other1 = arr[0];
			other2 = arr[2];
		}
		else
		{
			other1 = arr[0];
			other2 = arr[1];
		}
		if (max_v*max_v == other1 *other1 + other2 *other2)
		{
			cout << "right" << endl;

		}
		else
		{
			cout << "wrong" << endl;
		}
	}

}