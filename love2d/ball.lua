Ball = {}

function Ball:load()
  self.width = 18
  self.height = 18
  self.x = love.graphics.getWidth() / 2
  self.y = love.graphics.getHeight() / 2
  self.speed = 200
  self.xvel = -self.speed
  self.yvel = 0
  self.Part = {}
  for x = 1,20 do
    self.Part[x] = {self.x, self.y}
  end
end

function Ball:update(dt)
  self.x = self.x + self.xvel * dt
  self.y = self.y + self.yvel * dt
  if self.y < 0 then
    self.y = 0
    self.yvel = -self.yvel
  elseif self.y + self.height > love.graphics.getHeight() then
    self.y = love.graphics.getHeight() - self.height
    self.yvel = -self.yvel
  end
  self:collision()
  table.remove(self.Part)
  table.insert(self.Part, 1, {self.x, self.y})
end

function Ball:collision()
  if CheckCollision(self, Player) then
    self.xvel = self.speed
    local middle_ball = self.y + self.height / 2
    local middle_player = Player.y + Player.height / 2
    local collision_pos = middle_ball - middle_player
    self.yvel = collision_pos * 5
  end
  if CheckCollision(self, Enemy) then
    self.xvel = -self.speed
    local middle_ball = self.y + self.height / 2
    local middle_enemy = Enemy.y + Enemy.height / 2
    local collision_pos = middle_ball - middle_enemy
    self.yvel = collision_pos * 5
  end
  if self.x < 0 then
    self.x = love.graphics.getWidth() / 2 - self.width / 2
    self.y = love.graphics.getHeight() / 2 - self.height / 2
    self.yvel = 0
    self.xvel = self.speed
    lifes = lifes - 1
  end
end

function Ball:colour(red, green, blue, alpha)
  love.graphics.setColor(1, 1, 1, 1)
end

function Ball:draw()
  for k,v in ipairs(self.Part) do
    if k ~= 1 then
      love.graphics.setColor(0.7, 0.7, 0.7, 0.5)
    end
    love.graphics.circle("fill", v[1], v[2], 15-k/2)
    love.graphics.setColor(1, 1, 1, 1)
  end
end
