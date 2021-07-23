const discord = require('discord.js');
require('dotenv').config();
const gnome_filter = require('./chatfilter.js');
const strawberry = new discord.Client({ partials: ['MESSAGE','CHANNEL','REACTION'] });
const SERVERID = '854423990147743764';
const aliveSince = new Date().getTime();
const emojis = ["🍓","🍊","🍋","🍐","🍏","🌊","💙","🔮","🌸","🌹","🧡","🐤","🍵","🐳","☄️","🍇","🌷","🐇","🐌","🖤",];
const roles = ["854552801699037234","854553087065849866","854553242196377601","854553422354579456","854553546078945330","854553960362410006","854554065059971073","854554285919567902","854554584000102420","854555504617062430","854555857853743176","854556118797647872","854556310049521684","854557105394810920","854556772555161611","854557296221880341","854557559384834049","854557721205932042","854558526826872862","854557886238687313"];
const hearts = ["♥️","🤎","🖤","💙","❤️","💛","💚","🤍","💝","💜","💖"];
var lastSentHeart = false;

function sendtoLogs(user, msg, slur, guild) {
    let logs = guild.channels.cache.find(ch => ch.id === "854438898523832320");
    var embed = new discord.MessageEmbed()
        .setTitle("Slur Detected")
        .setColor('#F99F9F')
        .setDescription(`${user.toString()} has used a slur. Slur: ||${slur}||`)
        .addField(`${user.tag}:`, `||${msg}||`)
        .setFooter(new Date());
    logs.send("<@&854431512173871105><@&854454178969288724><@&854439285129216020>");
    logs.send(embed);
}

strawberry.on('ready', () => {
    let server = strawberry.guilds.cache.find(g => g.id === SERVERID);
    console.clear();
    console.log(`
░██████╗░███╗░░██╗░█████╗░███╗░░░███╗███████╗
██╔════╝░████╗░██║██╔══██╗████╗░████║██╔════╝
██║░░██╗░██╔██╗██║██║░░██║██╔████╔██║█████╗░░
██║░░╚██╗██║╚████║██║░░██║██║╚██╔╝██║██╔══╝░░
╚██████╔╝██║░╚███║╚█████╔╝██║░╚═╝░██║███████╗
░╚═════╝░╚═╝░░╚══╝░╚════╝░╚═╝░░░░░╚═╝╚══════╝#8777\n\nLogged in as ${strawberry.user.tag}!`);
    strawberry.user.setActivity(`${server.name}`, {type: 'WATCHING'});
});

strawberry.on('guildMemberAdd', worm => {

    if (worm.user.bot) return;

    let channel = worm.guild.channels.cache.find(ch => ch.id === "854433022677483581");
    channel.send(`Welcome ${worm.user.toString()} to ${worm.guild.name}`);
    
    let role = worm.guild.roles.cache.find(r => r.id === "854443884285132871");
    worm.roles.add(role);

});

strawberry.on('message', juice => {

    if (juice.author == strawberry.user) return;
    lastSentHeart = false;
    let usedCommand = true;
    
    switch (juice.content.toLowerCase()) {
        case ".joke":
            let jokes = ["Why are frogs so happy... They eat whatever bugs them!","How does a frog feel when he has a broken leg... Unhoppy!","What happened to the frog's car when the meter expired... It was toad!","What's a frog's favorite game... Croaket!","What do frogs order at restaurants... French flies and a diet croak!"];
            let rand = Math.floor(Math.random() * jokes.length);
            juice.reply(jokes[rand]);
            break;

        case "ribbit":
            let rs = ['🍄','🌸','🍓','🌞'];
            let rando = Math.floor(Math.random() * rs.length);
            juice.react(rs[rando]);
            let replies = ["RIBBIT :frog:","𝓻𝓲𝓫𝓫𝓲𝓽~❀","𝓡-𝓡𝓲𝓫𝓫𝓲𝓽( ˘͈ ᵕ ˘͈♡)","kero kero~🍇","*ara ara*","Croak :beetle:"];
            rando = Math.floor(Math.random() * replies.length);
            juice.reply(replies[rando]);
            break;

        case ".h":
        case ".help":
            let success = true
            juice.author.send("**Here's a list of my commands! *ribbit***\n.alive - See how long I've been awake\nribbit - pong\n.help/.h - display commands\n.joke - I'll tell you a joke").catch((e) => {
                juice.react("❌");
                juice.reply("I cannot DM you! Please ensure your DMs are **OPEN**.");
                success = false;
            }).then(() => {
                if (success) juice.react("✅");
            });
            break;

        case ".alive":
            juice.react("🕝");
            var seconds, minutes, hours = 0;
            let min, hou = false;
            var end = new Date();
            var diff = end - aliveSince;
            diff /= 1000;
            seconds = Math.round(diff);
            if (seconds > 60) {
                minutes = Math.round(seconds/60);
                if (Math.round(seconds/60) > (seconds/60)) seconds = Math.round(seconds/60)-(seconds/60);
                else seconds = (seconds/60)-Math.round(seconds/60);
                seconds = Math.round(seconds*100);
                min = true;
            } 
            if (minutes > 60) {
                hours = Math.round(minutes/60);
                if (Math.round(minutes/60) > (minutes/60)) minutes = Math.round(minutes/60)-(minutes/60);
                else minutes = (minutes/60)-Math.round(minutes/60);
                minutes = Math.round(minutes*100);
                hou = true;
            }

            if (min && !hou) juice.channel.send(`Alive for ${minutes} minutes, and ${seconds} seconds!`);
            else if (hou) juice.channel.send(`Alive for ${hours} hours, ${minutes} minutes, and ${seconds} seconds!`);
            else juice.channel.send(`Alive for ${seconds} seconds!`);
            break;

        default:
            usedCommand = false; 
            break;
    };

    let filter = gnome_filter.filterWord(juice.content);
    if (filter[1] && juice.channel.type !== "dm") {
        juice.reply("The use of slurs are not allowed on the server... <@&854431512173871105>");
        sendtoLogs(juice.author, juice.content, filter[0], juice.guild);
        juice.delete();
    }

    // if (juice.content[0] === "." && !usedCommand && juice.content.length > 1 && juice.content.replace(".","")) juice.channel.send(`I don't know \"${juice.content}\", sorry... 😔`);

});

strawberry.on('messageReactionAdd', async (bush, worm) => {

    let server = strawberry.guilds.cache.find(g => g.id === SERVERID);
    if (bush.partial) {
        try {
            await bush.fetch();
		} catch (error) {
            console.error('FETCH ERROR: ', error);
			return;
		}
	}

    if (bush.message.id === "854586208550125569") { // reaction panel

        let role = null;
        let u = server.member(worm.id);
        let skip, found = false;
        
        for (let j = 0; j < emojis.length; j++) {
            if (bush.emoji.toString() === emojis[j]) {
                role = server.roles.cache.find(r => r.id === roles[j]);
                if (u.roles.cache.find(r => r.id === roles[j])) {
                    skip = true;
                    found = true;
                    break;
                }
                found = true;
                break;
            } else {
                continue;
            }
        }
        if (!found) {
            bush.remove();
            return;
        }
        if (!skip) {
            u.roles.add(role);
        }
        skip = false;
    } else if (hearts.includes(bush.emoji.toString()) && bush.message.author == strawberry.user && !lastSentHeart) { // juni message
        bush.message.channel.send(worm.toString() + ", Thanks for the love! 🤗");
        lastSentHeart = true;
    }
});

strawberry.on('messageReactionRemove', async (bush, worm) => {
    let server = strawberry.guilds.cache.find(g => g.id === SERVERID);
    let u = server.member(worm.id);

    if (bush.partial) {
        try {
            await bush.fetch();
		} catch (error) {
            console.error('FETCH EROR: ', error);
			return;
		}
	}

    if (bush.message.id === "854586208550125569") { // reaction pannel
        let role = null;
        let skip = false;
        for (let j = 0; j < emojis.length; j++) {
            if (bush.emoji.toString() === emojis[j]) {
                role = server.roles.cache.find(r => r.id === roles[j]);
                if (u.roles.cache.find(r => r.id === roles[j])) {
                    break;
                } else {
                    skip = true;
                    break;
                }
            } else {
                continue;
            }
        }
        if (!skip) {
            u.roles.remove(role);
        }
        skip = false;
    }
});

strawberry.login(process.env.D_TOKEN);