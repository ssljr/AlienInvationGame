class Setting:
    """存储外星人入侵的所有设置的类"""

    def __init__(self):
        """初始化游戏设置"""
        # 初始化屏幕
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)
        # 初始左右移动化速度
        self.ship_center_speed = 1.5

        """初始化子弹信息"""
        # 初始化子弹速度
        self.bullet_speed = 1
        # 初始化子弹像素宽度、高度、颜色、屏幕上子弹数量
        self.bullet_width = 3
        self.bullet_height = 5
        self.bullet_color = (00, 00, 00)
        self.bullet_allowed = 5

        # 子弹连续发射
        self.keep_shooting = False
