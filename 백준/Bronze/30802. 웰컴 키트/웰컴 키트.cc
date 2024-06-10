#include <iostream>
using namespace std;
int main()
{
	int arr[6];
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int num{}, cnt{};
	cin >> num;
	for (int i = 0; i < 6; i++)
	{
		cin >> arr[i];
	}
	int t{}, p{};
	cin >> t >> p;
	for (int i = 0; i < 6; i++)
	{
		if (arr[i] % t == 0)
		{
			cnt += arr[i] / t;
		}
		else
		{
			cnt += arr[i] / t + 1;
		}

	}
	cout << cnt << endl;
	cout << num / p << " " << num % p << endl;

	return 0;
}