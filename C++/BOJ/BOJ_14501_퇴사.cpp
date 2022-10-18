#include <iostream>
using namespace std;

// [A] ���� ���� ����
int N, result;
int* T;
int* P;

// [B] DFS �Լ� ����
void dfs(int start, int money)
{
	// [B-1] ����ġ�� ����. N+1���� �ѱ�� �״�� �����Ѵ�.
	if (start > N + 1)
	{
		return;
	}
	// [B-2] ���� ����. N+1�Ͽ� �����ϸ� money�� result���� ���Ѵ�.
	else if (start == N + 1)
	{
		if (result < money)
		{
			result = money;
		}
		return;
	}

	dfs(start + T[start], money + P[start]); // ���� ����� ��� ���
	dfs(start + 1, money); // ���� ����� ���� �ʴ� ���
	
}


// [1] �Է°� ����
int main()
{
	cin >> N;
	
	// [1-1] ���� �Ҵ����� T�� P �迭�� ����� ���� �޴´�.
	T = new int[N + 1];
	P = new int[N + 1];
	for (int i = 1; i < N + 1; i++)
	{
		cin >> T[i];
		cin >> P[i];
	}

	// [2] DFS Ž�� �� ���
	dfs(1, 0);
	cout << result << endl;

	// [1-2] �޸� ���� ������ ���� �޸� ����
	delete[] T;
	delete[] P;

	return 0;
}
