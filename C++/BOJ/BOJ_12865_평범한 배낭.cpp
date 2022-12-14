#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// [A] ���� ���� ����
int N, K;
vector<int> DP;


int main()
{
	// [1] �Է°� ����
	cin >> N >> K;

	for (int i = 0; i <= K; i++)
	{
		DP.push_back(0);
	}

	// [2] 1���� DP Ǯ��
	//     K���� W���� �������� DP[i](= ��������� �ִ밪)�� V+DP[i-W](= �̹� ������ ������ �ִ밪)�� ���Ѵ�.
	for (int n = 0; n < N; n++)
	{
		int W, V;
		cin >> W >> V;

		for (int i = K; i >= W; i--)
		{
			DP[i] = max(DP[i], V + DP[i - W]);
		}
	}

	cout << DP[K] << endl;
	return 0;
}
