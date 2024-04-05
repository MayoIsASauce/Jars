use std::{
    path::Path, 
    path::PathBuf, env
};

pub fn get_path(file: &str) -> PathBuf {
    let fname = Path::new(file);
    let current_dir = env::current_exe().expect("current exe failed");

    let mut main_path = current_dir.parent().expect("unable to return parent <1>");
    while !main_path.ends_with("blackjack") {
        main_path = main_path.parent().expect("unable to unwrap parent <2>");
    }

    main_path.join(fname)
}