#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// [A] ���� ���� ����
int N, K, S, X, Y;
vector<vector<int>> tube;

int main()
{
	// [1] �Է°� ����
	cin >> N >> K;
	tube.assign(N, vector<int>(N));
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			cin >> tube[i][j];
		}
	}
	cin >> S >> X >> Y;
	
	// [2] (x, y) ĭ�� �������� ���̷����� �����ϴ��� ã�´�.
	int x = X - 1;
	int y = Y - 1;

	// [2-1] ���� (x, y)ĭ�� ���̷����� �̹� �ִٸ� ����Ѵ�.
	if (tube[x][y])
	{
		cout << tube[x][y];
	}
	// [2-2] (x, y)���� �Ÿ��� 1�� �÷����� ���̷����� �ִ��� Ž���Ѵ�.
	// ���̷����� �߰��ϸ� �ּڰ��� ����ϰ�, ������ �߰����� ���ϸ� 0�� ����Ѵ�.
	else
	{
		vector<int> virus;
		int flag = 1;
		for (int n = 1; n <= S; n++)
		{

			for (int i = x-n; i <= x+n; i++)
			{
				for (int j = y-n; j <= y+n; j++)
				{
					if (0 <= i && i < N && 0 <= j && j < N && abs(x - i) + abs(y - j) == n && tube[i][j])
					{
						virus.push_back(tube[i][j]);
					}
				}
			}
			if (virus.size())
			{
				int min = *min_element(virus.begin(), virus.end());
				cout << min << '\n';
				break;
			}
		}

		if (virus.size() == 0)
		{
			cout << 0;
		}
	}
	return 0;
}
