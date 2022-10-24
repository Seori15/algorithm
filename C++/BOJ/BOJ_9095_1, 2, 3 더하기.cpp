#include <iostream>
#include <vector>
using namespace std;

// DP Ǯ��
// ���� ���� ����
int T, N;
vector<int> DP;

int main()
{
	cin >> T;
	for (int tc = 1; tc <= T; tc++)
	{
		cin >> N;

		// DP[0]���� DP[3]�� �ʱⰪ�� ����.
		DP.push_back(0);
		DP.push_back(1);
		DP.push_back(2);
		DP.push_back(4);

		// ���� DP[4]���� DP[N]������ ���ǿ� �°� ���� �־��ش�.
		for (int i = 4; i <= N; i++)
		{
			DP.push_back(DP[i - 1] + DP[i - 2] + DP[i - 3]);
		}

		// DP[N] ���
		cout << DP[N] << '\n';

	}
	return 0;
}