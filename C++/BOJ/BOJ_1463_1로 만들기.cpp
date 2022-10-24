#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

// DP Ǯ��
// ���� ���� ����
int N;
vector<int> DP;

int main()
{
	cin >> N;

	// DP[0]�� DP[1]�� �ʱⰪ 0�� ����.
	DP.push_back(0);
	DP.push_back(0);

	// ���� DP[2]���� DP[N]������ ���ǿ� �°� ���� �־��ش�.
	// 2�� 3�� ������ �ش� DP[i/2] Ȥ�� DP[i/3] +1��, �̿ܿ��� DP[i-1]+1�� �ִ´�.
	for (int i = 2; i <= N; i++)
	{
		DP.push_back(DP[i - 1] + 1);
		if (i % 2 == 0)
		{
			DP[i] = min(DP[i], DP[i / 2] + 1);
		}
		if (i % 3 == 0)
		{
			DP[i] = min(DP[i], DP[i / 3] + 1);
		}
	}
	
	// DP[N] ���
	cout << DP[N];

	return 0;
}