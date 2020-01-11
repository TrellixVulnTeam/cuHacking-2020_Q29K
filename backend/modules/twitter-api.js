const fs = require('fs');

const Twitter = require('twit');
const twitterApi = JSON.parse(fs.readFileSync('../config/twitter.json', 'utf-8'));
 
const twitter = new Twitter({
  consumer_key: twitterApi.consumerKey,
  consumer_secret: twitterApi.consumerSecret,
  access_token: twitterApi.accessTokenKey,
  access_token_secret: twitterApi.accessTokenSecret
});

getTweets('rbc');

function getTweets(account) {
    twitter.get('search/tweets', { q: `@${account} since:2019-01-01 -filter:retweets`, tweet_mode: 'extended', count: 100 }, function(err, data, response) {
        let tweets = [];
        data.statuses.forEach(tweet => {
            tweets.push({
                id: tweet.id,
                text: tweet.full_text,
                created_at: tweet.created_at,
                user_name: tweet.user.name,
                user_screen_name: tweet.user.screen_name,
                user_profile: tweet.user.profile_image_url
            });
        });
        // fs.writeFileSync('./tweets.json', JSON.stringify(tweets));
        console.log(tweets);
    });
}