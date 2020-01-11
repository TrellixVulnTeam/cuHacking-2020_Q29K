import { Injectable } from '@angular/core';
import { CanActivate, Router } from '@angular/router';
import { AuthService } from '../services/auth.service';

@Injectable({
  providedIn: 'root'
})
export class AuthGuard implements CanActivate {

  constructor(private authenticationService: AuthService, private router: Router) { }

  async canActivate() {
    const user = await this.authenticationService.getFirebaseUser();
    if (!user) {
      this.router.navigate(['authentication']);
      return false;
    }
    return true;
  }

}
