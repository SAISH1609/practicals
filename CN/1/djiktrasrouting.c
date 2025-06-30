#include <stdio.h>
#define MAX 10
#define INF 999
int distance[MAX][MAX];
int n;
int next_vertex(int dist[], int visited[])
{
    int min = INF, min_index = -1, i;
    for (i = 0; i < n; i++)
    {
        if (!visited[i] && dist[i] < min)
        {
            min = dist[i];
            min_index = i;
        }
    }
    return min_index;
}
void dijkstra(int src, int dest)
{
    int dist[MAX], visited[MAX], parent[MAX], next_hop[MAX], i, v;
    for (i = 0; i < n; i++)
    {
        dist[i] = INF;
        visited[i] = 0;
        parent[i] = -1;
        next_hop[i] = -1;
    }
    dist[src] = 0;
    for (i = 0; i < n - 1; i++)
    {
        int u = next_vertex(dist, visited);
        if (u == -1)
            break;
        visited[u] = 1;
        for (v = 0; v < n; v++)
        {
            if (!visited[v] && dis tance[u][v] != INF && dist[u] + distance[u][v] < dist[v])
            {
                dist[v] = dist[u] + distance[u][v];
                parent[v] = u;
                if (u == src)
                    next_hop[v] = v;
                else
                    next_hop[v] = next_hop[u];
            }
        }
    }
    printf("\nRouting Table for Source Node %d:\n", src);
    printf("%-10s %-15s %-10s\n", "Dest", "Shortest Dist", "Next Hop");
    for (i = 0; i < n; i++)
    {
        if (i == src)
            continue;
        if (dist[i] == INF)
            printf("%-10d %-15s %-10s\n", i, "INF", "--");
        else
            printf("%-10d %-15d %-10d\n", i, dist[i], next_hop[i]);
    }
    if (dist[dest] == INF)
    {
        printf("\nNo path exists from %d to %d.\n", src, dest);
    }
    else
    {
        printf("\nShortest Distance from %d to %d: %d\n", src, dest, dist[dest]);
        int path[MAX], path_index = 0;
        for (v = dest; v != -1; v = parent[v])
        {
            path[path_index++] = v;
        }
        printf("Path: ");
        for (i = path_index - 1; i >= 0; i--)
        {
            printf("%d", path[i]);
            if (i > 0)
                printf(" -> ");
        }
        printf("\n");
    }
}

int main()
{
    int max_edges, origin, destin, dist, src, dest, i, j;
    printf("Enter number of nodes: ");
    scanf("%d", &n);
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n; j++)
        {
            if (i == j)
                distance[i][j] = 0;
            else
                distance[i][j] = INF;
        }
    }
    max_edges = n * (n - 1);
    for (i = 1; i <= max_edges; i++)
    {
        printf("\nEnter origin as -1 and destination as -1 to end\n");
        printf("Enter edge %d (Origin Destination): ", i);
        scanf("%d %d", &origin, &destin);
        if (origin == -1 && destin == -1)
            break;
        printf("Enter Distance: ");
        scanf("%d", &dist);

        if (origin >= n || destin >= n || origin < 0 || destin < 0)
        {
            printf("Invalid edge! Try again.\n");
            i--;
        }
        else
        {
            distance[origin][destin] = dist;
            distance[destin][origin] = dist;
        }
    }
    printf("Enter Source Vertex: ");
    scanf("%d", &src);
    printf("Enter Destination Vertex: ");
    scanf("%d", &dest);
    dijkstra(src, dest);

    return 0;
}
