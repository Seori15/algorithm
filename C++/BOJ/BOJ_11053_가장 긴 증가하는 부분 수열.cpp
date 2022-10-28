#include <iostream>
#include <algorithm>
using namespace std;

// ���� ���� ����
int N, A[1000], check[1000];

int main()
{
	// [1] �Է°� ����
	cin >> N;
	for (int i = 0; i < N; i++)
	{
		cin >> A[i];
		check[i] = 1;
	}

	// [2] DP Ǯ��. ���� A�� �� i ��ġ���� j ��ġ ���� ���� ��
	// i�� ���ڰ� �� ũ�ٸ� check[i]�� �� �� �����Ѵ�.
	for (int i = 1; i < N; i++)
	{
		for (int j = 0; j < i; j++)
		{
			if (A[i] > A[j])
			{
				check[i] = max(check[i], check[j] + 1);
			}
		}
	}

	// [3] check�� ��� ���� ū ���� ����Ѵ�.
	cout << *max_element(check, check+N) << '\n';
	return 0;
}