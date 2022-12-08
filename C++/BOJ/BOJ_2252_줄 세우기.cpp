#include <iostream>
#include <vector>
using namespace std;

// [A] ���� ���� ����
int N, M;
vector<int> check(32001, 0);
vector<int> ans;

int main()
{
	// [1] �Է°� ����
	cin >> N >> M;

	// [2] M�� �ٿ��� �־����� �л��� a, b��� ���� ��,
	//     a�� ans �տ�, b�� �ڿ� ����� check ó���Ѵ�.
	for (int i = 0; i < M; i++)
	{
		int a, b;
		cin >> a >> b;
		if (check[a] == 0)
		{
			check[a] = 1;
			ans.insert(ans.begin(), a);
		}
		if (check[b] == 0)
		{
			check[b] = 1;
			ans.push_back(b);
		}
	}

	// [3] ������ ������ ����(check ó������ ����) �л����� �߰��Ѵ�.
	for (int i = 1; i < N + 1; i++)
	{
		if (check[i] == 0)
		{
			ans.push_back(i);
		}
	}

	// [4] ans�� ����Ѵ�.
	for (int i = 0; i < N; i++)
	{
		cout << ans[i] << ' ';
	}
	return 0;
}
