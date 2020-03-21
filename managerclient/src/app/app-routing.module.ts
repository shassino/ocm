import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { AdminComponent } from './admin/admin.component';
import { UsersComponent } from './users/users.component';
import { MatchesComponent } from './matches/matches.component';
import { LeagueComponent } from './league/league.component';
import { StatsComponent } from './stats/stats.component';
import { RulesComponent } from './rules/rules.component';
import { HomeComponent } from './home/home.component';
import { LoginComponent } from './login/login.component';


const routes: Routes = [
  { path: 'admin', component: AdminComponent },
  { path: 'league', component: LeagueComponent },
  { path: 'matches', component: MatchesComponent },
  { path: 'rules', component: RulesComponent },
  { path: 'stats', component: StatsComponent },
  { path: 'users', component: UsersComponent },
  { path: 'home', component: HomeComponent },
  { path: 'login', component: LoginComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
