#include "../lib/template.cpp"
#include <string>

#define INF 0x3f3f3f3f

typedef pair<int, int> iPair;

class Graph {
  int V;

  list<iPair> *adj;

public:
  Graph(int V);

  void addEdge(int u, int c, int v, int w);

  int shortestPath(int s);
};
Graph::Graph(int V) {
  this->V = V;
  adj = new list<iPair>[V];
}

void Graph::addEdge(int u, int c, int v, int w) {
  adj[u].push_back(make_pair(v, w));
  adj[v].push_back(make_pair(u, c));
}

int Graph::shortestPath(int src) {
  priority_queue<iPair, vector<iPair>, greater<iPair>> pq;

  vector<int> dist(V, INF);

  pq.push(make_pair(0, src));
  dist[src] = 0;

  while (!pq.empty()) {
    int u = pq.top().second;
    pq.pop();

    list<pair<int, int>>::iterator i;
    for (i = adj[u].begin(); i != adj[u].end(); ++i) {
      int v = (*i).first;
      int weight = (*i).second;

      if (dist[v] > dist[u] + weight) {
        dist[v] = dist[u] + weight;
        pq.push(make_pair(dist[v], v));
      }
    }
  }

  return dist[V - 1];
}

int main() {
  f file("15/set.txt");

  int r = 0;
  vector<string> rows;
  vector<string> rows_big;

  string line;
  while (getline(file, line)) {
    rows.push_back(line);
  }

  FOR(i, rows) {
    string row = rows[i];
    string row_big = row;
    string new_row, saved_row = row;
    FOR(4) {
      new_row = "";
      FOR(k, saved_row) {
        int n = saved_row[k] - '0';
        n++;
        if (n > 9)
          n = 1;
        new_row += to_string(n);
      }
      row_big += new_row;
      saved_row = new_row;
    }
    rows_big.push_back(row_big);
  }

  vector<string> last_rows = rows;
  FOR(4) {
    vector<string> rows_current = last_rows;

    FOR(i, rows_current) {
      FOR(k, rows_current[i]) {
        int n = rows_current[i][k] - '0';
        n++;
        if (n > 9)
          n = 1;
        rows_current[i][k] = n + '0';
      }
    }

    FOR(i, rows_current) {
      string row = rows_current[i];
      string row_big = row;
      string new_row, saved_row = row;
      FOR(4) {
        new_row = "";
        FOR(k, saved_row) {
          int n = saved_row[k] - '0';
          n++;
          if (n > 9)
            n = 1;
          new_row += to_string(n);
        }
        row_big += new_row;
        saved_row = new_row;
      }
      rows_big.push_back(row_big);
    }

    last_rows = rows_current;
  }

  int elem_num = rows_big.size() * rows_big[0].size();
  Graph g(elem_num);

  int graph_pos = 0;
  FOR(i, rows_big) {
    string row = rows_big[i];
    FOR(j, row) {
      int pos_right = (graph_pos + 1) % row.size() != 0 ? graph_pos + 1 : -1;
      int pos_bottom =
          (graph_pos + row.size()) < elem_num ? graph_pos + row.size() : -1;
      int weight_right = row[j + 1] - '0';
      int weight_bottom = rows_big[i + 1][j] - '0';
      int current_weight = row[j] - '0';

      if (pos_right != -1) {
        g.addEdge(graph_pos, current_weight, pos_right, weight_right);
      }
      if (pos_bottom != -1) {
        g.addEdge(graph_pos, current_weight, pos_bottom, weight_bottom);
      }

      graph_pos++;
    }
  }

  int result = g.shortestPath(0);
  cout << result << endl;
}
