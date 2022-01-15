package com.company;

import javax.sound.sampled.*;
import javax.swing.*;
import java.util.Random;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import javax.imageio.ImageIO;
import javax.swing.Timer;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.net.URISyntaxException;
import java.time.Duration;
import java.time.Instant;
import java.util.*;
import java.util.List;

public class GamePanel extends JPanel implements ActionListener
{
    private Timer timer;
    private Random random = new Random();

    private int ego_dx;
    private int ego_dy;

    private boolean BEGIN_ENDING = false;
    private boolean GAME_HAS_ENDED = false;

    private int cam_rot = 0;
    private final int max_rot = -3138;
    private final int min_rot = 0;

    private int distance = 0;
    private final int max_distance = 50;

    private final String[] credits = {"Visual Design", "Graphical Art", "Character Design", "Character Scripting", "Lead Developer", "Head of Technical Gameplay",
            "Systems Engineer", "Sound Effects", "Sound Engineer", "That One Guy Who Doesn't Do Work in a Group", "Intern", "Testing", "Head of Testing", "Imagineer", "3D Engine Developer",
            "Marketing Executive", "CEO", "CFO", "Resident Cool Guy", "Algorithm Engineer", "Story Boarder", "Adam Sandler", "\"The Rock\"", "Choreographer", "Current US President",
            "Bench Warmer", "Technical Lead", "Hardware Engineer", "Inspiration", "Special Thank you", "Matt", "Over-Caffeinated", "Tired", "Programmer", "Lead Programmer",
            "Professional Slacker", "In-house Doctor", "Cat Wrangler", "Accountant", "Million Dollar Man", "Psychiatrist", "Therapist", "Flat Earther", "Team Captain", "Lead Mobile Developer",
            ".NET Developer", "Network Administrator", "Content Moderator", "Criminal Lawyer", "Gnome-City Mayor", "Gnome", "System.out.Println(\"Matt\") outputs", "Senior", "Counselor",
            "Python Consultant", "Do You Get the Joke Yet?", "Who?"
    };
    private final String[] prefixes = {"Senior ", "Junior ", "", "", ""};
    private List<credits_line> active_credits = new ArrayList<>();
    private int drawing_epochs = 0;

    private int[] title = new int[2];
    private boolean first_run = true;

    BufferedImage overlay;
    BufferedImage autograph;
    BufferedImage hover;
    BufferedImage e_button;

    Image kitty;
    boolean[] kitty_down = {false, true};
    Point[] kitty_points = {new Point(0, 150), new Point(530, 150)}; // 0, 530

    Clip walking_sfx;
    Clip pickup_sfx;
    Clip chicken_dance;
    Clip cheering;

    Instant first;
    Instant end;

    _dialogHandler dialog = new _dialogHandler();
    boolean cancel_dialog = true;
    String current_line;

    Dimension screen_info;
    int epochs = 0;

    private final _objects[] all_objects = {
            new _objects("rock.gif", new Point(1000, 150), new Dimension(200, 200), 1),
            new _objects("bloodrush.png", new Point(2600, 150), new Dimension(200, 200), 0),
    };

    private _objects player_holding = null;

    private void setStaticImages() {
        try {
            overlay = ImageIO.read(Objects.requireNonNull(getClass().getResource("Illustration26.png")));
            autograph = ImageIO.read(Objects.requireNonNull(getClass().getResource("Illustration31.png")));
            hover = ImageIO.read(Objects.requireNonNull(getClass().getResource("without_napkin.png")));
            e_button = ImageIO.read(Objects.requireNonNull(getClass().getResource("e_button.png")));
            kitty = new ImageIcon(Objects.requireNonNull(getClass().getResource("kitty.gif"))).getImage().getScaledInstance(250, 200, Image.SCALE_DEFAULT);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private void set_sfx() {
        try {
            AudioInputStream a_in = AudioSystem.getAudioInputStream(new File(Objects.requireNonNull(getClass().getResource("walking.wav")).toURI()).getAbsoluteFile());
            walking_sfx = AudioSystem.getClip();
            walking_sfx.open(a_in);
            a_in = AudioSystem.getAudioInputStream(new File(Objects.requireNonNull(getClass().getResource("pickup.wav")).toURI()).getAbsoluteFile());
            pickup_sfx = AudioSystem.getClip();
            pickup_sfx.open(a_in);
            a_in = AudioSystem.getAudioInputStream(new File(Objects.requireNonNull(getClass().getResource("chicken.wav")).toURI()).getAbsoluteFile());
            chicken_dance = AudioSystem.getClip();
            chicken_dance.open(a_in);
            a_in = AudioSystem.getAudioInputStream(new File(Objects.requireNonNull(getClass().getResource("cheer.wav")).toURI()).getAbsoluteFile());
            cheering = AudioSystem.getClip();
            cheering.open(a_in);
        } catch (UnsupportedAudioFileException | IOException | LineUnavailableException | URISyntaxException e) {
            e.printStackTrace();
        }
    }

    public class _dialogHandler {
        private List<String> queued = new ArrayList<>();
        public int amount_passed = 0;

        public void add_to_queue(String line) {
            queued.add(line);
        }
        public void add_to_queue(String[] lines) {
            queued.addAll(Arrays.asList(lines));
        }
        public String get_next() {
            String next = queued.get(0);
            amount_passed++;
            queued.remove(0);
            return next;
        }
    }

    public class credits_line {
        public String credit;
        public Point point;
        public credits_line(String credit, Point point) {
            this.credit = credit;
            this.point = point;
        }
    }

    public class _objects {
        public Image sprite;
        public String name;
        public Point location;
        public Dimension size;
        private Dimension original_size;
        public boolean hidden = false;
        private int interaction_type = 0;

        public _objects(String path_to_image, Point location, Dimension size, int interaction_type) {
            sprite = new ImageIcon(Objects.requireNonNull(getClass().getResource(path_to_image))).getImage().getScaledInstance(size.width, size.height, Image.SCALE_DEFAULT);
            this.location = location;
            this.size = size;
            original_size = size;
            this.interaction_type = interaction_type;
            name = path_to_image;
        }
        public void interact() {
            switch (interaction_type) {
                case 0: // item
                    this.hidden = true;
                    player_holding = this;
                    if (pickup_sfx.isActive()) pickup_sfx.stop();
                    pickup_sfx.start();
                    break;
                case 1: // npc
                    // 9
                    switch (dialog.amount_passed) {
                        case 12:
                            break;
                        case 10:
                            BEGIN_ENDING = true;
                            cheering.start();
                        case 9:
                            if (player_holding != all_objects[1]) break;
                        default:
                            current_line = dialog.get_next();
                    }
                    break;
                default:
                    break;
            }
        }
    }

    private void start_walking() {
        if (BEGIN_ENDING) return;
        walking_sfx.loop(100);
        walking_sfx.start();
    }
    private void stop_walking() {
        walking_sfx.stop();
    }

    public GamePanel()
    {
        ego_dx = 0;
        ego_dy = 0;
        timer = new Timer(10, this);
        timer.start();
        first = Instant.now();
        setFocusable(true);
        requestFocusInWindow();
        TAdapter keyhandler = new TAdapter();
        addKeyListener(keyhandler);
        setStaticImages();
        set_sfx();
//        GAME_HAS_ENDED = true;
        screen_info = getSize();
        title[0] = 245;
        title[1] = 275;

        dialog.add_to_queue(new String[] {"Yo, it's me the rock", "...", "So you're (insert name here)", "Nice to meet you (insert name here)", "What's that you want my autograph", "...",
                "Sure kid, but first you have to get me my BloodRush™", "It's the protein powder behind you", "Get me that and I'll give you whatever", "Wow you really did it, nice.",
                "Ok here you go, you earned it."});
        current_line = dialog.get_next();
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        // THIS CODE IS RUN EVERY 10 MS when the "timer" goes off
        // THIS IS THE GAME LOOP
        if (!BEGIN_ENDING && epochs > 50 || screen_info == null || screen_info.width == 0) {
            screen_info = getSize();
            epochs = 0;
        } else if (epochs > 500 && BEGIN_ENDING) {
            end = Instant.now();
            GAME_HAS_ENDED = true;
            epochs = 0;
        } else if (!GAME_HAS_ENDED) {
            epochs++;

            cam_rot += -ego_dx;
            distance += ego_dy;

            cancel_dialog = ego_dy != 0 || ego_dx != 0;

            if (ego_dy != 0 || ego_dx != 0) start_walking();
            else stop_walking();

            if (distance > max_distance)
                distance = max_distance;
            if (distance < -max_distance)
                distance = -max_distance;

            if (cam_rot < max_rot)
                cam_rot = min_rot;
            if (cam_rot > min_rot)
                cam_rot = max_rot;
        }

        if (GAME_HAS_ENDED) drawing_epochs++;
        repaint();
    }

    @Override
    public void paintComponent(Graphics g) {
        super.paintComponent(g);

        Polygon poly;
        if (GAME_HAS_ENDED) {

            if (!chicken_dance.isActive()) {
                chicken_dance.loop(100);
                chicken_dance.start();
            }

            g.setColor(new Color(236,242,250));
            g.fillRect(-10,-10, screen_info.width+10, screen_info.height+10);
            g.setColor(Color.BLACK);

            Duration elapsed = Duration.between(first, end);

            int kitty_speed = 2;
            for (int i = 0; i < 2; i++) {
                if (kitty_down[i]) {
                    kitty_points[i].y += kitty_speed;
                    if (kitty_points[i].y+200 >= screen_info.height) {
                        kitty_points[i].y = screen_info.height-200;
                        kitty_down[i] = false;
                    }
                } else {
                    kitty_points[i].y -= kitty_speed;
                    if (kitty_points[i].y <= 0) {
                        kitty_points[i].y = 0;
                        kitty_down[i] = true;
                    }
                }
                g.drawImage(kitty, kitty_points[i].x, kitty_points[i].y, null);
            }
//            final String[] credit_names = {"Matt", "Matt", "Matt", "Matt", "Matt", "Bree"};
            if (!first_run) {
                long seconds = elapsed.toSeconds();
                while (seconds >= 60) seconds -= 60;
                long minutes = elapsed.toMinutes();
                while (minutes >= 60) minutes -= 60;

                if (drawing_epochs > 20 && active_credits.size() < 30) {
                    active_credits.add(new credits_line(prefixes[random.nextInt(prefixes.length)]+credits[random.nextInt(credits.length)]+
                            ": Matt", new Point(screen_info.width/2-120, screen_info.height)));
                    for (int i = 0; i < active_credits.size(); i++) {
                        credits_line cursor = active_credits.get(i);
                        cursor.point.y -= 1;
                        g.setFont(new Font("Comic Sans MS", Font.BOLD, 14));
                        g.drawString(cursor.credit, cursor.point.x, cursor.point.y);

                        if (cursor.point.y < 0) active_credits.remove(i);
                    }
                    drawing_epochs = 0;
                } else if (active_credits.size() > 0){
                    for (int i = 0; i < active_credits.size(); i++) {
                        credits_line cursor = active_credits.get(i);
                        cursor.point.y -= 1;
                        g.setFont(new Font("Comic Sans MS", Font.BOLD, 14));
                        g.drawString(cursor.credit, cursor.point.x, cursor.point.y);

                        if (cursor.point.y < 0) active_credits.remove(i);
                    }

                    title[0] -= 1;
                    title[1] -= 1;

                    g.drawString("Time taken: "+Integer.toString((int)elapsed.toHours())+":"+Integer.toString((int)minutes)+":"+Integer.toString((int)seconds), screen_info.width/2-120, title[1]);
                    g.setFont(new Font("Comic Sans MS", Font.BOLD, 32));
                    g.drawString("Made by Matt", screen_info.width/2-120,title[0]);
                }
            } else {
                if (drawing_epochs > 500) first_run = false;
                g.setFont(new Font("Comic Sans MS", Font.BOLD, 32));
                g.drawString("Made by Matt", screen_info.width/2-120,title[0]);
                g.setFont(new Font("Comic Sans MS", Font.BOLD, 14));
                g.drawString("Time taken: "+Integer.toString((int)elapsed.toHours())+":"+Integer.toString((int)elapsed.toMinutes())+":"+Integer.toString((int)elapsed.toSeconds()), screen_info.width/2-120, title[1]);

            }

        } else {

            int margin = 50;
            g.setFont(Font.getFont("Arial"));


            for (int i = 0; i < 5; i++) { // FOREACH WALL

                switch (i) {
                    case 1:
                        g.setColor(Color.green);
                        break;
                    case 2:
                        g.setColor(Color.RED);
                        break;
                    case 3:
                        g.setColor(Color.MAGENTA);
                        break;
                    case 4:
                    case 0:
                    default:
                        g.setColor(Color.BLUE);
                        break;
                }

                poly = new Polygon();
                int poly_x = (screen_info.width * i) + cam_rot;
                int poly_x2 = screen_info.width + (screen_info.width * i) + cam_rot;


                // opposite down
                // To bring the offset up - instead of +
                //            offset_y1 = margin + Math.abs(cam_rot);
                //            offset_y2 = margin + cam_rot;
                //            if (offset_y1 > 185) offset_y1 = 185;
                //            if (offset_y2 < margin) offset_y2 = margin;


                int[] offsets = {0, 0, 0, 0};
                if ((poly_x >= -30 && poly_x <= 30)
                        || (poly_x >= screen_info.width - 30 && poly_x <= screen_info.width + 30)
                        || ((poly_x2 >= -30 && poly_x2 <= 30))
                        || (poly_x2 >= screen_info.width - 30 && poly_x2 <= screen_info.width + 30)) {
                    offsets[0] = margin;
                    offsets[1] = margin;
                    offsets[2] = screen_info.height - margin;
                    offsets[3] = screen_info.height - margin;
                } else if (poly_x < 0) {
                    offsets[0] = margin;
                    offsets[1] = margin * 2;
                    offsets[3] = screen_info.height - margin;
                    offsets[2] = screen_info.height - margin * 2;
                } else {
                    offsets[0] = margin * 2;
                    offsets[1] = margin;
                    offsets[3] = screen_info.height - margin * 2;
                    offsets[2] = screen_info.height - margin;
                }

                poly.addPoint(poly_x, offsets[0] + distance);
                poly.addPoint(poly_x2, offsets[1] + distance);
                poly.addPoint(poly_x2, offsets[2] - distance);
                poly.addPoint(poly_x, offsets[3] - distance);
                if ((poly_x >= 0 && poly_x <= screen_info.width)
                        || (poly_x2 >= 0 && poly_x2 <= screen_info.width))
                    g.fillPolygon(poly);
            }

            for (_objects obj : all_objects) {
                if (obj.hidden) continue;
                g.drawImage(obj.sprite, (obj.location.x + cam_rot), (obj.location.y), null);
            }

            if (BEGIN_ENDING) g.drawImage(autograph, 0, 0, null);
            else {
                boolean skip = false;
                for (int i = 0; i < all_objects.length; i++)
                    if (touching_sprite(all_objects[i], screen_info.width/2) && !all_objects[i].hidden) skip = true;
                if (skip) g.drawImage(hover, +5, +20, null);
                else g.drawImage(overlay, 0, -20, null);
            }

            g.setColor(Color.BLACK);

            if (touching_sprite(all_objects[0], screen_info.width / 2)) {
                Polygon temp = new Polygon();

                temp.addPoint(100, 350);
                temp.addPoint(700, 350);
                temp.addPoint(700, 450);
                temp.addPoint(100, 450);

                g.fillPolygon(temp);

                g.setColor(Color.WHITE);
                g.setFont(new Font("Verdana", Font.BOLD, 18));
                g.drawString(current_line, 120, 390);

                g.drawImage(e_button, 650, 400, null);
            }

            //        g.setFont(new Font("Arial", Font.PLAIN, 11));
            //        g.setColor(Color.BLACK);
            //        g.drawString("cam_rot: "+cam_rot, 0, 20);
            //        g.drawString("distance: "+distance, 0, 30);

            g.setColor(Color.WHITE);
            g.drawOval(screen_info.width / 2, screen_info.height / 2, 10, 10);
        }
    }

    public boolean touching_sprite(_objects obj, int x_to_check) {
        Rectangle _tmp = new Rectangle(new Point(obj.location.x+cam_rot, obj.location.y+cam_rot), obj.size);
        return ((x_to_check > _tmp.getLocation().x && x_to_check < _tmp.getLocation().x+_tmp.width));
    }


    private class TAdapter extends KeyAdapter {

        @Override
        public void keyReleased(KeyEvent e) {
            if(e.getKeyCode() == KeyEvent.VK_LEFT)
            {
                ego_dx=0;
            }
            if(e.getKeyCode() == KeyEvent.VK_RIGHT)
            {
                ego_dx=0;
            }
            if(e.getKeyCode() == KeyEvent.VK_UP)
            {
                ego_dy=0;
            }
            if(e.getKeyCode() == KeyEvent.VK_DOWN)
            {
                ego_dy=0;
            }
        }

        @Override
        public void keyPressed(KeyEvent e) {
            if (e.getKeyCode() == KeyEvent.VK_E)
            {
                if (GAME_HAS_ENDED) return;
                // interaction check
                for (_objects obj : all_objects) {
                    if (touching_sprite(obj, screen_info.width/2))
                        obj.interact();
                }
            }
            int look_speed = 5;
            if(e.getKeyCode() == KeyEvent.VK_LEFT)
            {
                ego_dx=-look_speed;
            }
            if(e.getKeyCode() == KeyEvent.VK_RIGHT)
            {
                ego_dx= look_speed;
            }
            if(e.getKeyCode() == KeyEvent.VK_UP)
            {
               ego_dy=-look_speed;
            }
            if(e.getKeyCode() == KeyEvent.VK_DOWN)
            {
              ego_dy= look_speed;
            }
        }
    }
}