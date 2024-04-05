
use crate::utils;

use std::process::Command;
use std::io::{Error, Write};
use std::process::{Stdio, Child};

pub fn start_python() -> Child {
    Command::new("python3")
        .arg(utils::get_path("python/main.py").to_str().unwrap())
        .stdin(Stdio::piped())
        .spawn()
        .expect("Unable to open python child")
}

pub fn send_python(python: &mut Child, content: String) -> Result<(), Error>{
    if let Some(ref mut stdin) = python.stdin {
        match stdin.write_all((content + "\n").as_bytes()) {
            Ok(_) => (),
            Err(err) => return Err(err),
        }
        stdin.flush().expect("Unable to flush python stdin");
    }
    Ok(())
}