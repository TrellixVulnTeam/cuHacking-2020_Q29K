import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { AuthService } from './services/auth.service';

@Component({
  selector: 'app-auth',
  templateUrl: './auth.component.html',
  styleUrls: ['./auth.component.css']
})
export class AuthComponent implements OnInit {

  public user;
  public page = 'sign-in';

  public signInForm: FormGroup = new FormGroup({
    email: new FormControl('', [Validators.required]),
    password: new FormControl('', [Validators.required])
  });

  public createAccountForm: FormGroup = new FormGroup({
    email: new FormControl('', [Validators.required]),
    password: new FormControl('', [Validators.required]),
    confirmPassword: new FormControl('', [Validators.required])
  });

  constructor(private authService: AuthService, private router: Router) { }

  async ngOnInit() {
    this.user = await this.authService.getFirebaseUser();
    if (this.user) {
      this.router.navigate(['dashboard']);
    }
  }

  public switchPage(page) {
    this.page = page;
  }

  public async trySignIn(data) {
    console.log(data);
    if (this.signInForm.status === 'VALID') {
      await this.authService.doSignIn(data.email, data.password)
        .then(() => this.router.navigate(['dashboard']))
        .catch(err => console.log(err));
    }
  }

  public async tryCreateAccount(data) {
    console.log(data);
    if (this.createAccountForm.status === 'VALID' && data.password === data.confirmPassword) {
      await this.authService.doRegister(data.email, data.password)
        .then(() => this.router.navigate(['dashboard']))
        .catch(err => console.log(err));
    }
  }

}
