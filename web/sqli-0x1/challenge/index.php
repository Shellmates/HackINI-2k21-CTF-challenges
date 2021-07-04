<?php
error_reporting(0);
error_log(0);

require_once("flag.php");

function is_trying_to_hak_me($str)
{   
    $blacklist = ["' ", " '", '"', "`", " `", "` ", ">", "<"];
    if (strpos($str, "'") !== false) {
        if (!preg_match("/[0-9a-zA-Z]'[0-9a-zA-Z]/", $str)) {
            return true;
        }
    }
    foreach ($blacklist as $token) {
        if (strpos($str, $token) !== false) return true;
    }
    return false;
}

if (isset($_GET["pls_help"])) {
    highlight_file(__FILE__);
    exit;
}
   
if (isset($_POST["user"]) && isset($_POST["pass"]) && (!empty($_POST["user"])) && (!empty($_POST["pass"]))) {
    $user = $_POST["user"];
    $pass = $_POST["pass"];
    if (is_trying_to_hak_me($user)) {
        die("why u bully me");
    }

    $db = new SQLite3("/var/db.sqlite");
    $result = $db->query("SELECT * FROM users WHERE username='$user'");
    if ($result === false) die("pls dont break me");
    else $result = $result->fetchArray();

    if ($result) {
        $split = explode('$', $result["password"]);
        $password_hash = $split[0];
        $salt = $split[1];
        if ($password_hash === hash("sha256", $pass.$salt)) $logged_in = true;
        else $err = "Wrong password";
    }
    else $err = "No such user";
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Hack.INI 9th - SQLi</title>
</head>
<body>
    <?php if (isset($logged_in) && $logged_in): ?>
    <p>Welcome back admin! Have a flag: <?=htmlspecialchars($flag);?><p>
    <?php else: ?>
    <form method="post">
        <input type="text" placeholder="Username" name="user" required>
        <input type="password" placeholder="Password" name="pass" required>
        <button type="submit">Login</button>
        <br><br>
        <?php if (isset($err)) echo $err; ?>
    </form>
    <?php endif; ?>
    <!-- <a href="/?pls_help">get some help</a> -->
</body>
</html>
