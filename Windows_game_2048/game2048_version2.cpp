#include <iostream>
#include <vector>
#include <conio.h>
#include <time.h>
using namespace std;

vector<vector<int>> pre = {{0, 0, 0, 0}, {0, 0, 0, 0}, {0, 0, 0, 0}, {0, 0, 0, 0}};
vector<vector<int>> pas = {{0, 0, 0, 0}, {0, 0, 0, 0}, {0, 0, 0, 0}, {0, 0, 0, 0}};
int score = 0;
int newscore = 0;
bool GAMEOVER = false;
int step = 0;
bool canback = true;

int create()
{
    vector<pair<int, int>> vp;
    for (int i = 0; i < 4; i++)
        for (int j = 0; j < 4; j++)
            if (pre[i][j] == 0)
                vp.push_back(pair<int, int>(i, j));
    int l = vp.size();
    if (!vp.size())
    {
        return 1; // No Empty quare
    }
    srand((unsigned int)time(NULL));
    int p = rand() % l;
    int q = rand() % 4;
    switch (q)
    {
    case 0:
    case 1:
    case 2:
        pre[vp[p].first][vp[p].second] = 2;
        break;
    case 3:
        pre[vp[p].first][vp[p].second] = 4;
        break;
    }
    return 0; // return success
}

void print()
{
    cout << "*************\n上移 : w or  ↑\n左移 : a or  ←\n右移 : d or  →\n下移 : s or  ↓\n倒退 : b\n*************\n";
    if (GAMEOVER)
    {
        cout << "\n\n    ---GAME OVER---\n    ----YOUR SCORE: " << score << "----\n    ----YOUR HAVE MOVED: " << step << " TIMES----" << endl;
        cout << "\n\n    ----PRESS 'R' TO RETRY---\n    ----PRESS 'E' TO EXIT----" << endl;
        cout << "\nBY THE WAY, THIS IS YOUR RELIC (OuO)" << endl;
        for (int i = 0; i < 4; i++)
        {
            for (int j = 0; j < 4; j++)
            {
                if (pre[i][j] == 0)
                    cout << "   囗";
                else
                    printf("%5d", pre[i][j]);
            }
            cout << endl;
        }
        return; // GAMEOVER
    }
    cout << "SCORE: " << score << endl;
    cout << "STEP: " << step << endl;
    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            if (pre[i][j] == 0)
                cout << "   囗";
            else
                printf("%5d", pre[i][j]);
        }
        cout << endl;
    }
}

int main()
{
ReStart:
    // initialize
    if (system("CLS"))
        system("clear");
    pre = {{0, 0, 0, 0}, {0, 0, 0, 0}, {0, 0, 0, 0}, {0, 0, 0, 0}};
    pas = {{0, 0, 0, 0}, {0, 0, 0, 0}, {0, 0, 0, 0}, {0, 0, 0, 0}};
    score = 0;
    newscore = 0;
    GAMEOVER = false;
    step = 0;
    canback = true;

    create();
    print();
    while (true)
    {
        if (_kbhit())
        {
            int ch;
            ch = getch();
            if (ch == 72 || ch == 'w')
            {
                newscore = 0;
                pas = pre;
                for (int i = 1; i < 4; i++)
                {
                    for (int j = 0; j < 4; j++)
                    {
                        if (!pre[i][j])
                            continue;
                        int n = pre[i][j];
                        for (int x = i - 1; x >= 0; x--)
                        {
                            if (pre[x][j] == 0)
                            {
                                if (x != 0)
                                    continue;
                                pre[i][j] = 0;
                                pre[x][j] = n;
                                break;
                            }
                            else if (pre[x][j] == n)
                            {
                                pre[i][j] = 0;
                                pre[x][j] = 2 * n;
                                score += 2 * n;
                                newscore += 2 * n;
                                break;
                            }
                            else
                            {
                                if (x + 1 != i)
                                pre[i][j] = 0;
                                pre[x + 1][j] = n;
                                break;
                            }
                        }
                    }
                }
                if (!create())
                {
                    step++;
                    canback = true;
                }
                if (system("CLS"))
                    system("clear");
            }
            else if (ch == 75 || ch == 'a')
            {
                newscore = 0;
                pas = pre;
                for (int j = 1; j < 4; j++)
                {
                    for (int i = 0; i < 4; i++)
                    {
                        if (!pre[i][j])
                            continue;
                        int n = pre[i][j];
                        for (int x = j - 1; x >= 0; x--)
                        {
                            if (pre[i][x] == 0)
                            {
                                if (x != 0)
                                    continue;
                                pre[i][j] = 0;
                                pre[i][x] = n;
                                break;
                            }
                            else if (pre[i][x] == n)
                            {
                                pre[i][j] = 0;
                                pre[i][x] = 2 * n;
                                score += 2 * n;
                                newscore += 2 * n;
                                break;
                            }
                            else
                            {
                                if (x + 1 != j)
                                pre[i][j] = 0;
                                pre[i][x + 1] = n;
                                break;
                            }
                        }
                    }
                }
                if (!create())
                {
                    step++;
                    canback = true;
                }
                if (system("CLS"))
                    system("clear");
            }
            else if (ch == 77 || ch == 'd')
            {
                newscore = 0;
                pas = pre;
                for (int j = 2; j >= 0; j--)
                {
                    for (int i = 0; i < 4; i++)
                    {
                        if (!pre[i][j])
                            continue;
                        int n = pre[i][j];
                        for (int x = j + 1; x < 4; x++)
                        {
                            if (pre[i][x] == 0)
                            {
                                if (x != 3)
                                    continue;
                                pre[i][j] = 0;
                                pre[i][x] = n;
                                break;
                            }
                            else if (pre[i][x] == n)
                            {
                                pre[i][j] = 0;
                                pre[i][x] = 2 * n;
                                score += 2 * n;
                                newscore += 2 * n;
                                break;
                            }
                            else
                            {
                                if (x - 1 != j)
                                pre[i][j] = 0;
                                pre[i][x - 1] = n;
                                break;
                            }
                        }
                    }
                }
                if (!create())
                {
                    step++;
                    canback = true;
                }
                if (system("CLS"))
                    system("clear");
            }
            else if (ch == 80 || ch == 's')
            {
                newscore = 0;
                pas = pre;
                for (int i = 2; i >= 0; i--)
                {
                    for (int j = 0; j < 4; j++)
                    {
                        if (!pre[i][j])
                            continue;
                        int n = pre[i][j];
                        for (int x = i + 1; x < 4; x++)
                        {
                            if (pre[x][j] == 0)
                            {
                                if (x != 3)
                                    continue;
                                pre[i][j] = 0;
                                pre[x][j] = n;
                                break;
                            }
                            else if (pre[x][j] == n)
                            {
                                pre[i][j] = 0;
                                pre[x][j] = 2 * n;
                                score += 2 * n;
                                newscore += 2 * n;
                                break;
                            }
                            else
                            {
                                if (x - 1 != i)
                                pre[i][j] = 0;
                                pre[x - 1][j] = n;
                                break;
                            }
                        }
                    }
                }
                if (!create())
                {
                    step++;
                    canback = true;
                }
                if (system("CLS"))
                    system("clear");
            }
            else if (ch == 'B'|| ch == 'b')
            {
                if(!step)
                    continue;
                if (!canback)
                    continue;
                step--;
                canback = false;
                pre = pas;
                score -= newscore;
                newscore = 0;
                if (system("CLS"))
                    system("clear");
            }
            else if (ch == 'E' || ch == 'e')
            {
                cout << "ARE YOU SEUR TO EXIT?  YOUR PLAYING DATA WILL NOT BE SAVE!\nPRESS 'Y' TO EXIT" << endl;
                while(true)
                {
                    if (_kbhit())
                    {
                        int ch;
                        ch = getch();
                        if (ch == 'Y' || ch == 'y')
                            return 1;
                        else
                        {
                            if (system("CLS"))
                                system("clear");
                            break;
                        }
                    }
                }
            }
            else
                continue;
            // gameover?
            bool alive = false; // alive or die
            for (int i = 0; i <4 && !alive; i++)
            {
                for (int j = 0; j<4 && !alive; j++)
                {
                    if (!pre[i][j])
                        alive = true;
                    
                    if (i != 0)
                        if(pre[i - 1][j] == pre[i][j])
                            alive = true;
                    if (i != 3)
                        if (pre[i + 1][j] == pre[i][j])
                    if (j != 0)
                        if (pre[i][j - 1] == pre[i][j])
                            alive = true;
                    if (j != 3)
                        if (pre[i][j + 1] == pre[i][j])
                            alive = true;
                }
            }
            if (!alive)
                GAMEOVER = true;
            print();
            if (GAMEOVER)
                break;
        }
    }
    while(true)
    {
        if (_kbhit())
        {
            int ch;
            ch = getch();
            if (ch == 'R' || ch == 'r')
                goto ReStart;
            else if (ch == 'E' || ch == 'e')
                return 0;
        }
    }
}