const fs = require('fs');

const Twitter = require('twit');
const twitterApi = JSON.parse(fs.readFileSync('./config/twitter.json', 'utf-8'));
 
const twitter = new Twitter({
  consumer_key: twitterApi.consumerKey,
  consumer_secret: twitterApi.consumerSecret,
  access_token: twitterApi.accessToken,
  access_token_secret: twitterApi.accessTokenSecret
});

module.exports.getTweets = async function getTweets(handle, maxId) {
    if (maxId == 0) {
        return new Promise(function(resolve, reject) {
            twitter.get('search/tweets', { q: `@${handle} since:2019-01-01 -filter:retweets`, tweet_mode: 'extended', count: 100 }, function(err, data, response) {
                let tweets = [];
                for (let i = 0; i < data.statuses.length; i++) {
                    const tweet = data.statuses[i];
                    tweets.push({
                        id: tweet.id,
                        text: tweet.full_text,
                        created_at: tweet.created_at,
                        user_name: tweet.user.name,
                        user_screen_name: tweet.user.screen_name,
                        user_profile_image: tweet.user.profile_image_url
                    });
                }
                resolve({tweets, next_results: data.search_metadata.next_results});
            });
        }).then(data => {
            return data;
        });
    } else {
        return new Promise(function(resolve, reject) {
            twitter.get('search/tweets', { q: `@${handle} since:2019-01-01 -filter:retweets`, tweet_mode: 'extended', count: 100, max_id: maxId }, function(err, data, response) {
                let tweets = [];
                for (let i = 0; i < data.statuses.length; i++) {
                    const tweet = data.statuses[i];
                    tweets.push({
                        id: tweet.id,
                        text: tweet.full_text,
                        created_at: tweet.created_at,
                        user_name: tweet.user.name,
                        user_screen_name: tweet.user.screen_name,
                        user_profile_image: tweet.user.profile_image_url
                    });
                }
                resolve({tweets, next_results: data.search_metadata.next_results});
            });
        }).then(data => {
            return data;
        });
    }
}
