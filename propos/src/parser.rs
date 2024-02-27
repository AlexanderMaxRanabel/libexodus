use colored::*;
use std::{
    process,
    fs::File,
    io::{BufRead, BufReader},
};

pub fn tokenizer(line: String) -> Vec<String> {
    let str_tokens: Vec<&str> = line.split_whitespace().collect();
    let tokens: Vec<String> = str_tokens.iter().map(|&s| s.to_owned()).collect();
    return tokens;
}

pub fn parser(file: String, mut stack: Vec<String>) -> anyhow::Result<()> {
    let file = File::open(file)?;
    let reader = BufReader::new(file);

    for line in reader.lines() {
        let line = line?;
        if !line.ends_with(";") {
            println!("{}: Line Does not end with ; : {}", "Error".red(), line.clone());
            process::exit(1);
        }
        let tokens = tokenizer(line.clone());
        let main_keyword = tokens.get(0).cloned().unwrap_or_else(|| {
            std::process::exit(1);
        });

        match main_keyword {
            "let" => {
               unimplemented!(); 
            },

            _ => {
                println!("{}: Unknown keyword: {}", "Error".red(), main_keyword);
                process::exit(1);
            },
        }
    }

    Ok(())
}
