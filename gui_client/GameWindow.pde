class GameWindow implements Window{
    private gui_client parent;
    private int bWidth;
    private int bHeight;
    private int tileSize;
    private int xBias;
    private int yBias;

    GameWindow(gui_client parent){
        this.parent = parent;

        this.bWidth = 20;
        this.bHeight = 20;
        this.tileSize = min(80, int(800 / max(bWidth, bHeight)));
        this.xBias = (800 - tileSize * bWidth) / 2;
        this.yBias = (800 - tileSize * bHeight) / 2;
    }

    void start(){
        // do nothing
    }

    void finish(){
        // do nothing
    }

    void draw(){
        background(255);

        // Board
        for(int y = 0; y < this.bHeight; ++ y){
            for(int x = 0; x < this.bWidth; ++ x){
                rect(x * this.tileSize + this.xBias,    // x
                     y * this.tileSize + this.yBias,    // y
                     this.tileSize, this.tileSize);     // size
            }
        }
    }
}