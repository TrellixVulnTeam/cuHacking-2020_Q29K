import { Injectable } from '@angular/core';
import { CanActivate, Router } from '@angular/router';
import { AuthService } from '../services/auth.service';

@Injectable({
  providedIn: 'root'
})
export class NotAuthGuard implements CanActivate {

  constructor(private authenticationService: AuthService, private router: Router) { }

  async canActivate() {
    const user = await this.authenticationService.getFirebaseUser();
    if (user) {
      this.router.navigate(['dashboard']);
      return false;
    }
    return true;
  }

}
