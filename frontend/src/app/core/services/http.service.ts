import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';

import { throwError } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class HttpService {

  private handleError(error: HttpErrorResponse) {
    if (error.error instanceof ErrorEvent) {
      console.error('An error occurred:', error.error.message);
    } else {
      console.error(`Backend returned code ${error.status}, ` + `body was: ${error.error}`);
    }
    return throwError('Something bad happened; please try again later.');
  }

  constructor(private http: HttpClient) { }

  getTweets(account, maxId = 0) {
    return this.http.get(decodeURI('http://localhost/api/get-tweets/' + account + '-' + maxId))
      .pipe(retry(3), catchError(this.handleError)).toPromise();
  }

}
