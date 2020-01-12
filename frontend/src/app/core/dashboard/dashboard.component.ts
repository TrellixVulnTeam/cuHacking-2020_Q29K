import { Component, OnInit } from '@angular/core';
import { AuthService } from '../../auth/services/auth.service';
import { Router } from '@angular/router';
import { HttpService } from '../services/http.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})
export class DashboardComponent implements OnInit {

  public maxId;
  public tweets = [];
  public tweetsData;

  constructor(private authService: AuthService, private router: Router, private httpService: HttpService) { }

  ngOnInit() {
      this.getTweets('rbc');
  }

  public async getTweets(account, maxId = 0) {
    this.tweetsData = await this.httpService.getTweets(account, maxId);
    this.maxId = this.tweetsData.next_results;
    this.maxId = this.maxId.substring(this.maxId.indexOf('max_id=') + 7, this.maxId.indexOf('&'));
    this.tweets.length !== 0 ? this.tweets = this.tweets.concat(this.tweetsData.tweets) : this.tweets = this.tweetsData.tweets;
    console.log(this.tweets);
  }

  public trySignOut() {
    this.authService.doSignOut();
    this.router.navigate(['auth']);
  }

}
