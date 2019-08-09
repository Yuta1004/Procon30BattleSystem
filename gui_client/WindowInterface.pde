interface Window{
    void start();
    void draw();
    void finish();
    void handleButtonEvents(GButton button, GEvent event);
    void handleTextEvents(GEditableTextControl textcontrol, GEvent event);
    void keyPressed();
    void keyReleased();
}