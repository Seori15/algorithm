#include <string.h>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int adjL[101][101];
int visited[101];

// [A] �� ��������� ����� ����ž ������ ��ȯ�ϴ� bfs �Լ�
int N;
int bfs(int i) {
    int cnt = 0;
    queue<int> q;
    q.push(i);
    while (!q.empty()) {
        cnt++;
        int now = q.front();
        q.pop();
        for (int next = 1; next <= N; next++) {
            if (adjL[now][next] && !visited[next]) {
                visited[next] = 1;
                q.push(next);
            }
        }
    }
    return cnt;
}

int solution(int n, vector<vector<int>> wires) {
    int answer = n;
    N = n;

    // [1] wires ������踦 adjL�� ����
    for (int i = 0; i < wires.size(); i++) {
        int A = wires[i][0];
        int B = wires[i][1];
        adjL[A][B] = adjL[B][A] = 1;
    }

    // [2] wires�� �� wire�� �ϳ��� ���´ٰ� �����Ͽ� ����Ž��.
    //     wire�� A�� B�� visitedó���ϰ� bfsŽ���ϸ� ������ ���̸� ���� �� �ִ�.
    for (int i = 0; i < wires.size(); i++) {
        memset(visited, 0, sizeof(visited));
        int A = wires[i][0];
        int B = wires[i][1];
        visited[A] = 1;
        visited[B] = 1;
        answer = min(answer, abs(n - 2 * bfs(A)));
    }
    return answer;
}