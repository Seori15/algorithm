#include <iostream>
#include <vector>
using namespace std;

// [A] �������� ����
int M, N;
vector<vector<int>> arr;
vector<vector<int>> visited;
int di[4] = {-1, 1, 0, 0};
int dj[4] = {0, 0, -1, 1};

// [B] dfs �Լ� ����
int dfs(int i, int j)
{
	// [B-1] ��Ʈ��ŷ ����. �̹� Ž���� ���� �ִٸ� visited�� ����� ���� ��ȯ.
	if (visited[i][j] != -1)
	{
		return visited[i][j];
	}
	// [B-2] ��� ���� ����. (M-1, N-1) ĭ�� �����ߴٸ� 1�� ��ȯ.
	if (i == M - 1 && j == N - 1)
	{
		return 1;
	}
	
	// [B-3] Top-Down ����. Ž���� �� ���� (i, j)�� ���� ���� ������ ���ش�.
	// visited[i][j]�� ����� ���� (i, j)���� (M-1, N-1) ĭ�� ������ �� �ִ� ����� ���̴�.
	// Ž���� �� ���� visited�� �⺻���� 0���� ���� �ʰ� -1�� �� ������ ����� ���� ��ĥ �� ���������� �����̴�.
	// ���� ���� visited�� -1�� �ƴ��� Ȯ���� ��, ���� 0���� �ʱ�ȭ�س��� ����� ���� ����Ѵ�.
	visited[i][j] = 0;
	for (int dr = 0; dr < 4; dr++)
	{
		int ni = i + di[dr], nj = j + dj[dr];
		if (0 <= ni && ni < M && 0 <= nj && nj < N && arr[i][j] > arr[ni][nj])
		{
			visited[i][j] += dfs(ni, nj);
		}
	}
	
	return visited[i][j];
}

// �Է°� ���� �� dfs Ž��
int main()
{
	cin >> M >> N;
	arr.assign(M, vector<int>(N));
	visited.assign(M, vector<int>(N));
	for (int i = 0; i < M; i++)
	{
		for (int j = 0; j < N; j++)
		{
			cin >> arr[i][j];
			visited[i][j] = -1;
		}
	}
	dfs(0, 0);
	cout << visited[0][0];
	return 0;
}
