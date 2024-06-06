#include <iostream>
#include <cmath>
using namespace std;

bool isPrime(int n) {
	if (n <= 1) return false;
	for (int i = 2; i <= sqrt(n); i++) {
		if (n % i == 0) return false;
	}
	return true;
}



int main(void)
{
    int num;
    cin >> num;
    int *arr= new int[num];
    int cnt = 0;
    // num 만큼 입력 받기
    for (int i = 0; i < num; i++) {
        cin >> arr[i];
    }

    // 입력된 수들 중 소수 찾기
    for (int i = 0; i < num; i++) {
        if (isPrime(arr[i])) {
            cnt += 1;
        }
    }
    cout << cnt << endl;
    return 0;
}