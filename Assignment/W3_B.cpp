#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class Node 
{
public:
	Node() { pre = NULL, result = 0, max = 0, second_max = 0; }; //초기값 0으로 설정, 중요!
	Node* pre;
	vector<int> data; //인접한 노드로의 length값
	vector<Node*> cnt; //인접한 노드들
	int result;
	int max, second_max;
};

void traversal(Node* node)
{
	if (node->pre == NULL) //node가 시작노드일 때
	{
		priority_queue<int> Q;

		for (int i = 0; i < node->cnt.size(); i++)
		{
			node->cnt[i]->pre = node;
			node->cnt[i]->result = node->result; //시작노드를 지나서 result값이 유지되어야 하므로 내려갈때도 가지고 가야됨
			traversal(node->cnt[i]);
			int n = node->data[i] + node->cnt[i]->max;
			Q.push(n);
		}

		if (node->cnt.size() == 1) //시작노드의 자식이 하나 밖에 없으면, 위의 for문 돌고 
								   //우선순위큐에 값이 하나밖에 들어있지 않음. 그래서 구분해줘야 됨
		{
			node->max = Q.top();
			Q.pop();
		}
		else
		{
			node->max = Q.top();
			Q.pop();
			node->second_max = Q.top();
		}
		int n = node->max + node->second_max;

		if (n > node->result)
		{
			cout << n << "\n";
		}
		else
		{
			cout << node->result << "\n";
		}
	}
	else if (node->cnt.size() == 1) //node가 leaf노드일 때
	{
		if (node->pre == node->cnt[0])
		{
			node->max = node->second_max = 0;
		}
	}
	else //노드가 시작노드, leaf노드도 아닐때 //중간 노드일 때
	{
		priority_queue<int> Q;
		for (int i = 0; i < node->cnt.size(); i++)
		{
			if (node->pre != node->cnt[i])
			{
				node->cnt[i]->pre = node;
				node->cnt[i]->result = node->result;
				traversal(node->cnt[i]);
				int n = node->data[i] + node->cnt[i]->max;
				Q.push(n);
			}
		}
		if (node->cnt.size() == 2) //노드의 자식이 하나 밖에 없으면, 위의 for문 돌고 
								   //우선순위큐에 값이 하나밖에 들어있지 않음. 그래서 구분해줘야 됨
		{
			node->max = Q.top();
			Q.pop();
		}
		else
		{
			node->max = Q.top();
			Q.pop();
			node->second_max = Q.top();
		}

		int n = node->max + node->second_max;
		if (n > node->result)
		{
			node->result = n;
		}
		node->pre->result = node->result; //result값 그대로 부모노드로 올리기

	}
	
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int T;
	cin >> T;
	while (T--)
	{
		int n;
		cin >> n;
		vector<Node> V(n + 1);
		for (int i = 1; i < n; i++)
		{
			int a, b, c;
			cin >> a >> b >> c;
			V[a].cnt.push_back(&V[b]);
			V[a].data.push_back(c);
			V[b].cnt.push_back(&V[a]);
			V[b].data.push_back(c);
		}

		traversal(&V[1]);
	}
}