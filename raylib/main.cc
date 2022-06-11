#include <raylib.h>

#define W 1200
#define H 720

struct Entity
{
  int x, y, w, h, xvel, yvel;
};

bool CheckCollision(struct Entity a, struct Entity b)
{
  if (a.x + a.w > b.x && a.x < b.x + b.w && a.y + a.h > b.y && a.y < b.y + b.h)
    return true;
  else return false;
}

int main(int argc, char** argv)
{
  Entity player; 
  player.x = 50;
  player.y = H / 2;
  player.w = 20;
  player.h = 100;
  player.xvel = 0;
  player.yvel = 10;

  Entity enemy;
  enemy.x = W - enemy.w - 50;
  enemy.y = H / 2;
  enemy.w = 20;
  enemy.h = 100;
  enemy.xvel = 0;
  enemy.yvel = 10;
  
  Entity ball;
  ball.x = W / 2;
  ball.y = H / 2;
  ball.w = 20;
  ball.h = 20;
  ball.xvel = 5;
  ball.yvel = 0;
  
  InitWindow(W, H, "Pong");
  SetTargetFPS(60);

  while (!WindowShouldClose())
  {
    if (IsKeyDown(KEY_UP)) player.y -= player.yvel;
    if (IsKeyDown(KEY_DOWN)) player.y += player.yvel;

    if (player.y < 0) player.y = 0;
    if (player.y + player.h > H) player.y = H - player.h;

    ball.x -= ball.xvel;
    ball.y -= ball.yvel;
    if (CheckCollision(ball, player))
      {
	ball.xvel = ball.xvel * -1;
	unsigned middle_ball = ball.y + ball.h / 2;
	unsigned middle_player = player.y + player.h / 2;
	unsigned collision_pos = middle_ball - middle_player;
	ball.yvel = collision_pos * 5;
      }
    
    BeginDrawing();
      ClearBackground(BLACK);
      DrawRectangle(player.x, player.y, player.w, player.h, RAYWHITE);
      DrawRectangle(enemy.x, enemy.y, enemy.w, enemy.h, RAYWHITE);
      DrawCircle(ball.x, ball.y, ball.w / 2, RAYWHITE);
    EndDrawing();
  }
  CloseWindow();

  return 0;
}
