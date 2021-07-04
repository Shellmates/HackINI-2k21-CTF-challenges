<?php
    $flag = "shellmates{1_r34lly_h0p3_u_d1dnt_us3_4n_aut0m4t3d_t0ol}";
    $secret_table = "t0t4lly_n0t_susp1ci10us";
    $username = "admin";
    $salt = bin2hex(random_bytes(4));
    $password_hash = hash("sha256", random_bytes(16));
    $db = new SQLite3("/var/db.sqlite");
    $db->exec("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)");
    $db->exec("INSERT INTO users VALUES ('$username', '$password_hash\$$salt')");
    $db->exec("CREATE TABLE IF NOT EXISTS $secret_table (flag TEXT)");
    $db->exec("INSERT INTO $secret_table VALUES ('$flag')");
    $db->close();
?>
