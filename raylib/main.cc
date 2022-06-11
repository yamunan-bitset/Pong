#include <raylib.h>

#define W 1200
#define H 720

struct Entity
{
  int x, y, w = 20, h = 100;
};

struct Ball
{
  int x, y, radius = 10;
};

int main(int argc, char** argv)
{
  const int vel = 10;
  Entity player; 
  player.x = 50;
  player.y = H / 2;
  Entity enemy;
  enemy.x = W - enemy.w - 50;
  enemy.y = H / 2;
  Ball ball;
  ball.x = W / 2;
  ball.y = H / 2;
  
  InitWindow(W, H, "Pong");
  SetTargetFPS(60);

  while (!WindowShouldClose())
  {
    if (IsKeyDown(KEY_UP)) player.y -= vel;
    if (IsKeyDown(KEY_DOWN)) player.y += vel;

    if (player.y < 0) player.y = 0;
    if (player.y + player.h > H) player.y = H - player.h;
    
    BeginDrawing();
      ClearBackground(BLACK);
      DrawRectangle(player.x, player.y, player.w, player.h, RAYWHITE);
      DrawRectangle(enemy.x, enemy.y, enemy.w, enemy.h, RAYWHITE);
      DrawCircle(ball.x, ball.y, ball.radius, RAYWHITE);
    EndDrawing();
  }
  CloseWindow();

  return 0;
}
