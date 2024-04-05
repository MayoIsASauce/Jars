mod python;
mod utils;
mod definitions;

use std::{thread::sleep, time::Duration};

use definitions::{Objects, GameObject};


fn main() {
    let mut objs = Objects {
        background: "255, 0, 0".to_string(),
        player: GameObject {
            x: 20,
            y: 20,
            w: 50,
            h: 50,
            color: (0, 255, 0),
        }
    };


    // starts
    let mut child = python::start_python();
    
    // interact
    let running: bool = true;
    while running {
        sleep(Duration::from_millis(50));
        objs.player.x += 5;
        objs.player.y += 5;
        let ser = serde_json::to_string(&objs).expect("Failed to serialize object");
        if python::send_python(&mut child, ser).is_err() {
            break;
        }
    }
    // ...

    // wait for python to end
    let _ = python::send_python(&mut child, "-1!".to_string());
    let e_code = child.wait().unwrap();
    println!("{}", e_code.to_string());
}