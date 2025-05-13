use tfhe::prelude::*;
use tfhe::{generate_keys, set_server_key, ConfigBuilder, FheInt64};
use std::time::Instant;

// Add for pmap
// use std::time::Duration;
// use std::thread::sleep;

const SCALE: f64 = 1e6;   

pub fn main() -> Result<(), Box<dyn std::error::Error>> {
    let config = ConfigBuilder::default().build();
    let (client_key, server_keys) = generate_keys(config);
    set_server_key(server_keys);

    let a = 1.23451256;
    let a_encode: i64 = (a * SCALE).round() as i64;
    let b = 6.78912312;
    let b_encode: i64 = (b * SCALE).round() as i64;

    let ctxt_a = FheInt64::encrypt(a_encode, &client_key);
    let ctxt_b = FheInt64::encrypt(b_encode, &client_key);

    let now = Instant::now();
    let ctxt_result = &ctxt_a + &ctxt_b;
    let elapsed = now.elapsed();
    println!("Temps d'exécution: {:?}", elapsed);

    let scaled_res: i64 = ctxt_result.decrypt(&client_key);
    let result: f64 = (scaled_res as f64) / SCALE;
    println!("{}", result);

    let result_prevu: f64 = a + b;
    println!("{}", result_prevu);

    let err_abs = (result - result_prevu).abs();
    let err_reel = err_abs / result_prevu.abs().max(1e-8);

    println!("Erreur absolue: {}", err_abs);
    println!("Erreur relative: {}", err_reel);
    
    //Add for pmap
    // println!("Addition terminée. Pause pour mesure mémoire...");
    // sleep(Duration::from_secs(120));

    Ok(())
}
