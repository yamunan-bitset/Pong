#include <raylib.h>

int main(int argc, char** argv)
{
  InitWindow(1200, 720, "Pong");
  SetTargetFPS(60);
  while (!WindowShouldClose())
  {
    BeginDrawing();
      ClearBackground(BLACK);
    EndDrawing();
  }
  CloseWindow();
  return 0;
}
