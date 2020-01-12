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

  public user;
  public handle;

  public page;

  public maxId;
  public tweets = [];
  public tweetsData;

  constructor(private authService: AuthService, private router: Router, private httpService: HttpService) { }

  ngOnInit() {
    this.page = 'all';
    this.getUser();
  }

  public async getUser() {
    const firebaseUser = await this.authService.getFirebaseUser();
    this.user = await this.httpService.getUser(firebaseUser.email);
  }

  public async getTweets(handle, maxId = 0) {
    if (handle === '') {
      const elem: any = document.getElementById('search');
      handle = elem.value;
    }
    if (maxId === 0 && handle !== this.handle && handle !== '') {
      this.tweets = [];
    }
    if (this.handle !== handle || maxId !== 0) {
      if (handle !== '') {
        this.handle = handle;
        this.tweetsData = await this.httpService.getTweets(handle, maxId);
        if (this.tweetsData.tweets.length !== 0) {
          this.maxId = this.tweetsData.next_results;
          this.maxId = this.maxId.substring(this.maxId.indexOf('max_id=') + 7, this.maxId.indexOf('&'));
          this.tweets.length !== 0 ? this.tweets = this.tweets.concat(this.tweetsData.tweets) : this.tweets = this.tweetsData.tweets;
        }
      }
    }
  }

  public async saveHandle() {
    if (this.handle !== '') {
      this.httpService.addHandle(this.user.email, this.handle);
      this.user.handles.push(this.handle);
    }
  }

  public async removeHandle(handle) {
    this.httpService.removeHandle(this.user.email, handle);
    this.user.handles.splice(this.user.handles.indexOf(handle), 1);
  }

  public setSearch(handle) {
    if (this.handle !== handle) {
      const elem: any = document.getElementById('search');
      elem.value = handle;
      this.getTweets(handle, 0);
    }
  }

  public trySignOut() {
    this.authService.doSignOut();
    this.router.navigate(['auth']);
  }

}
