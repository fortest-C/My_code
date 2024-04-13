#include <iostream>
#include <vector>
#include <conio.h>
#include <time.h>
#include <windows.h>
using namespace std;

vector<vector<int>> pre = {{0, 0, 0, 0}, {0, 0, 0, 0}, {0, 0, 0, 0}, {0, 0, 0, 0}};
vector<vector<int>> pas = {{0, 0, 0, 0}, {0, 0, 0, 0}, {0, 0, 0, 0}, {0, 0, 0, 0}};
int score = 0;
int newscore = 0;
bool GAMEOVER = false;
int step = 0;
bool canback = true;
int TOTLE_SCORE = 0;
int RUN_TIME = 0;

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
    cout << "SUM_SCORE:" << TOTLE_SCORE << endl;
    cout << "RUN TIMES:" << RUN_TIME << endl;
    cout << "AVERAGE: " << TOTLE_SCORE/RUN_TIME << endl;
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

#define BUTTON 'd'
#define DELAY 80
int button = 'w';

int main()
{
ReStart:
    RUN_TIME+=1;
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
        bool change = false;
        if(_kbhit())
        {
            int ch = getch();
            if (ch =='e' || ch == 'E')
                return 1;
        }
        Sleep( DELAY );
            //int ch = BUTTON;
            /**/
            int ch;
            switch(button)
            {
                case 'w': button = 'd'; ch = 'd'; break;
                case 'd': button = 's'; ch = 's'; break;
                case 's': button = 'a'; ch = 'a'; break;
                case 'a': button = 'w'; ch = 'w'; break;
            }
            /**/
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
                    change = true;
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
                    change = true;
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
                    change = true;
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
                    change = true;
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
            if (!alive || !change)
                GAMEOVER = true;
            print();
            if (GAMEOVER)
            {
                TOTLE_SCORE += score;
                break;
            }
    }
    goto ReStart;
}
