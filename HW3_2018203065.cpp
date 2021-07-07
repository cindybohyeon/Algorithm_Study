
/*** 2018203065 김보현 ***/

#include <iostream>
#include <cstring>
using namespace std;
#define MAXN 20
#define INF 987654321
char inputmap[MAXN][MAXN];
char makemap[MAXN][MAXN];//초기화
char made_map[MAXN][MAXN];
char remade_map[MAXN][MAXN];
char switch_map[MAXN][MAXN];
char reswitch_map[MAXN][MAXN];//최종 값을 저장
bool switched[MAXN];
int N;
int ans = INF;


int result = INF;
/*** 스위치 켜기/끄기 ***/
void switching(int x, int y, char arr[][MAXN]) {
    if (y > 0) {
        if (arr[x][y - 1] == 'O') {
            arr[x][y - 1] = '#';
        }
        else {
            arr[x][y - 1] = 'O';
        }
    }
    if (x < N - 1) {
        if (arr[x + 1][y] == 'O') {
            arr[x + 1][y] = '#';
        }
        else {
            arr[x + 1][y] = 'O';
        }
    }
    if (x > 0) {
        if (arr[x - 1][y] == 'O') {
            arr[x - 1][y] = '#';
        }
        else {
            arr[x - 1][y] = 'O';
        }
    }
    if (y < N - 1) {
        if (arr[x][y + 1] == 'O') {
            arr[x][y + 1] = '#';
        }
        else {
            arr[x][y + 1] = 'O';
        }
    }
    if (arr[x][y] == 'O') {
        arr[x][y] = '#';
    }
    else {
        arr[x][y] = 'O';
    }
}
void dfs(int select, int column) {
    int press = 0;
    memcpy(made_map, makemap, sizeof(makemap));
    memcpy(switch_map, makemap, sizeof(makemap));
    int sum = 0;
    for (int i = 0; i < N; i++) {//첫번째 행 전체 돌린다
        if (switched[i]) {//해당 경우에서 선택한 열만 스위칭 한다.
                switch_map[0][i] = 'O';
                //스위칭한 열을 표시한다
            press++;
            switching(0, i, made_map);//지도중, 첫번째 행의 경우의 수 
        }
    }
    for (int i = 1; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (made_map[i - 1][j] != inputmap[i - 1][j]) {//결과값이 같지 않을 경우, 
                    switch_map[i][j] = 'O';
                    //아래의 행에서 스위칭을 한다
                press++;
                switching(i, j, made_map);
            }
        }
    }
    bool flag = false;
    for (int i = 0; i < N && !flag; i++) {//맨 아래가 결과값이 같은 경우는 
        //모든 경우가 결과와 동일해진 것이기 때문에 
        //맨아래의 결과값만 확인한다
        if (made_map[N - 1][i] != inputmap[N - 1][i]) flag = true;//같지 않는다면 flag true으로 표시
    }//
    if (!flag && press < result) {
        result = press;
        ans = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                reswitch_map[i][j] = switch_map[i][j];
            }

        }
    }
    if (column == N) return;
    for (int i = select; i < N; i++) {
        if (!switched[i]) {//
            switched[i] = true;//i번째 원소 switch해준다
            dfs(i, column + 1);//몇번째 열까지 갔는지 +1 해준다
            switched[i] = false;//끝난 뒤, 다음을 위해서 false로 초기화
        }
    }
}
int main() {
    //cin의 컴파일 속도 향상시키기 위해서 씀
    ios::sync_with_stdio(false);
    cin.tie(0);

    /*** 입력 및 할당 ***/
    cin >> N;//(1)N입력
    for (int i = 0; i < N; i++) {//(2)N*N 만큼의 결과map 입력, 초기map 만들기
        for (int j = 0; j < N; j++) {
            cin >> inputmap[i][j];//결과map
            makemap[i][j] = '#';//초기map
        }
    }

    dfs(0, 0);

    /*** 출력 ***/
    if (ans != 0) {
        cout << "no solution\n";
       return 0;
    }
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cout << reswitch_map[i][j];
            cout << " ";
        }
        cout << "\n";
    }
    return 0;
}