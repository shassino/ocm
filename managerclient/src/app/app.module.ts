import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import {MatToolbarModule} from '@angular/material/toolbar';
import {MatButtonModule} from '@angular/material/button';
import { UsersComponent } from './users/users.component';
import { AdminComponent } from './admin/admin.component';
import { MatchesComponent } from './matches/matches.component';
import { LeagueComponent } from './league/league.component';
import { StatsComponent } from './stats/stats.component';
import { RulesComponent } from './rules/rules.component';
import { HomeComponent } from './home/home.component';
import { LoginComponent } from './login/login.component';


@NgModule({
  declarations: [
    AppComponent,
    UsersComponent,
    AdminComponent,
    MatchesComponent,
    LeagueComponent,
    StatsComponent,
    RulesComponent,
    HomeComponent,
    LoginComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatToolbarModule,
    MatButtonModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
