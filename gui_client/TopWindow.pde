class TopWindow{
    private PImage proconLogo;
    private GTextField tokenInputForm;
    private GButton tokenEnterButton;
    private gui_client parent;
    
    TopWindow(gui_client parent){
        this.parent = parent;
        
        // Load Assets
        proconLogo = loadImage("res/proconlogo.jpeg");
        
        // Create G4P Instance
        this.tokenInputForm = new GTextField(
            this.parent, 350, 550, 200, 20
        );
        this.tokenEnterButton = new GButton(
            this.parent, 300, 600, 200, 30, "START"
        );
        
        // Tag Set
        this.tokenInputForm.tag = "TokenInput";
        this.tokenEnterButton.tag = "ClientStart";
    }

    void topWindowDraw(){
        background(255);
        
        // Title Text
        textAlign(CENTER);
        fill(0);
        textSize(40);
        text("Procon30 Battle System", 400, 200);
        text("GUI Client", 400, 250);
        
        // Title Logo
        imageMode(CENTER);
        image(this.proconLogo, 400, 400);
        
        // TokenInputForm
        textSize(20);
        text("TOKEN:", 300, 568);
    }
}