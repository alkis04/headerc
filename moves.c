#include "printB.h"

int nMovesX[] = {-2, 2, -1, 1, -2, 2, -1, 1};
int nMovesY[] = {1, 1, 2, 2, -1, -1, -2, -2};

int kMovesX[] = {1, 1, 1, 0, 0, -1, -1, -1};
int kMovesY[] = {1, 0, -1, 1, -1, 1, 0, -1};

void genBishop(char **pos, int row, int col){
    int x = row + 1, y = col + 1;
    while(x <= 7 && y <= 7){
        if(pos[x][y]*pos[row][col] > 0){
            break;
        }
        if(pos[x][y]*pos[row][col] < 0){
            pos[x][y] = 7;
            break;
        }
        pos[x][y] = 7;
        ++x, ++y;
    }

    x = row - 1, y = col + 1;
    while(x >= 0 && y <= 7){
        if(pos[x][y]*pos[row][col] > 0){
            break;
        }
        if(pos[x][y]*pos[row][col] < 0){
            pos[x][y] = 7;
            break;
        }
        pos[x][y] = 7;
        --x, ++y;
    }

    x = row + 1, y = col - 1;
    while(x <= 7 && y >= 0){
        if(pos[x][y]*pos[row][col] > 0){
            break;
        }
        if(pos[x][y]*pos[row][col] < 0){
            pos[x][y] = 7;
            break;
        }
        pos[x][y] = 7;
        ++x, --y;
    }

    x = row - 1, y = col - 1;
    while(x >= 0 && y >= 0){
        if(pos[x][y]*pos[row][col] > 0){
            break;
        }
        if(pos[x][y]*pos[row][col] < 0){
            pos[x][y] = 7;
            break;
        }
        pos[x][y] = 7;
        --x; --y;
    }

    printBoard(pos);
}

void genKnight(char **pos, int row, int col){
    int x,y;
    for(int i = 0; i < 8; ++i){
        x = row + nMovesX[i];
        y = col + nMovesY[i];
        if(x < 0 || x > 7 || y < 0 || y > 7) continue;
        if(pos[x][y]*pos[row][col] > 0) continue; 
        pos[x][y] = 7;
    }
    printBoard(pos);
}

void genRook(char **pos, int row, int col){
    int x = row + 1, y = col;
    while(x <= 7){
        if(pos[x][y]*pos[row][col] > 0){
            break;
        }
        if(pos[x][y]*pos[row][col] < 0){
            pos[x][y] = 7;
            break;
        }
        pos[x][y] = 7;
        ++x;
    }

    x = row - 1;
    while(x >= 0){
        if(pos[x][y]*pos[row][col] > 0){
            break;
        }
        if(pos[x][y]*pos[row][col] < 0){
            pos[x][y] = 7;
            break;
        }
        pos[x][y] = 7;
        --x;
    }

    x = row, y = col + 1;
    while(y <= 7){
        if(pos[x][y]*pos[row][col] > 0){
            break;
        }
        if(pos[x][y]*pos[row][col] < 0){
            pos[x][y] = 7;
            break;
        }
        pos[x][y] = 7;
        ++y;
    }

    y = col - 1;
    while(y >= 0){
        if(pos[x][y]*pos[row][col] > 0){
            break;
        }
        if(pos[x][y]*pos[row][col] < 0){
            pos[x][y] = 7;
            break;
        }
        pos[x][y] = 7;
        --y;
    }

    printBoard(pos);
}

void genQueen(char **pos, int row, int col){
    int x = row + 1, y = col;
    while(x <= 7){
        if(pos[x][y]*pos[row][col] > 0){
            break;
        }
        if(pos[x][y]*pos[row][col] < 0){
            pos[x][y] = 7;
            break;
        }
        pos[x][y] = 7;
        ++x;
    }

    x = row - 1;
    while(x >= 0){
        if(pos[x][y]*pos[row][col] > 0){
            break;
        }
        if(pos[x][y]*pos[row][col] < 0){
            pos[x][y] = 7;
            break;
        }
        pos[x][y] = 7;
        --x;
    }

    x = row, y = col + 1;
    while(y <= 7){
        if(pos[x][y]*pos[row][col] > 0){
            break;
        }
        if(pos[x][y]*pos[row][col] < 0){
            pos[x][y] = 7;
            break;
        }
        pos[x][y] = 7;
        ++y;
    }

    y = col - 1;
    while(y >= 0){
        if(pos[x][y]*pos[row][col] > 0){
            break;
        }
        if(pos[x][y]*pos[row][col] < 0){
            pos[x][y] = 7;
            break;
        }
        pos[x][y] = 7;
        --y;
    }
    x = row + 1, y = col + 1;
    while(x <= 7 && y <= 7){
        if(pos[x][y]*pos[row][col] > 0){
            break;
        }
        if(pos[x][y]*pos[row][col] < 0){
            pos[x][y] = 7;
            break;
        }
        pos[x][y] = 7;
        ++x, ++y;
    }

    x = row - 1, y = col + 1;
    while(x >= 0 && y <= 7){
        if(pos[x][y]*pos[row][col] > 0){
            break;
        }
        if(pos[x][y]*pos[row][col] < 0){
            pos[x][y] = 7;
            break;
        }
        pos[x][y] = 7;
        --x, ++y;
    }

    x = row + 1, y = col - 1;
    while(x <= 7 && y >= 0){
        if(pos[x][y]*pos[row][col] > 0){
            break;
        }
        if(pos[x][y]*pos[row][col] < 0){
            pos[x][y] = 7;
            break;
        }
        pos[x][y] = 7;
        ++x, --y;
    }

    x = row - 1, y = col - 1;
    while(x >= 0 && y >= 0){
        if(pos[x][y]*pos[row][col] > 0){
            break;
        }
        if(pos[x][y]*pos[row][col] < 0){
            pos[x][y] = 7;
            break;
        }
        pos[x][y] = 7;
        --x; --y;
    }

    printBoard(pos);
}

void genKing(char **pos, int row, int col){
    int x,y;
    for(int i = 0; i < 8; ++i){
        x = row + kMovesX[i];
        y = col + kMovesY[i];
        if(x < 0 || x > 7 || y < 0 || y > 7) continue;
        if(pos[x][y]*pos[row][col] > 0) continue; 
        pos[x][y] = 7;
    }
    printBoard(pos);
}

void genPawn(char **pos, int row, int col){
    int start_pos;
    int move;
    if (pos[row][col] == 1){
        start_pos = 6;
        move = -1;
    }else{
        start_pos = 1;
        move = 1;
    }
    int x = row + move;
    int y = col;
    if (row < 7){
        if (!pos[x][y]){
            pos[x][y] = 7;
            x += move;
            if (row == start_pos && !pos[x][y]){
                pos[x][y] = 7;
            }
        }

        x = row + move;
        y = col - 1;
        if((pos[x][y])*(pos[row][col]) < 0){ 
            pos[x][y] = 7;
        }
        y = col + 1;
        if((pos[x][y])*(pos[row][col]) < 0){ 
            pos[x][y] = 7;
        }
    }
    printBoard(pos);
}

void genMoves(char **pos){
    int i, j;
    for(i = 0; i < 8; ++i){
        for(j = 0; j < 8; ++j){
            if(!pos[i][j]) continue;
            switch(pos[i][j]){
                case 1:
                    genPawn(pos, i, j);
                    break;
                case 2:
                    genKnight(pos, i, j);
                    break;
                case 3:
                    genBishop(pos, i, j);
                    break;
                case 4:
                    genRook(pos, i, j);
                    break;
                case 5:
                    genQueen(pos, i, j);
                    break;
                case 6:
                    genKing(pos, i, j);
                    break;
                case -1:
                    genPawn(pos, i, j);
                    break;
                case -2:
                    genKnight(pos, i, j);
                    break;
                case -3:
                    genBishop(pos, i, j);
                    break;
                case -4:
                    genRook(pos, i, j);
                    break;
                case -5:
                    genQueen(pos, i, j);
                    break;
                case -6:
                    genKing(pos, i, j);
                    break;
            }
        }
    }
}