package com.company;

import javax.swing.*;
import java.awt.*;


public class Main extends JFrame {

    public Main()
    {
        add(new GamePanel());
        setSize(800,500);
        setTitle("Matt's 3D Adventure");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setResizable(false);
    }
    public static void main(String[] args) {
        EventQueue.invokeLater(() -> {
            Main ex = new Main();
            ex.setVisible(true);
        });
    }
}
