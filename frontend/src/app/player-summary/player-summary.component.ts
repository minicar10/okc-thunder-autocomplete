import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { PlayerSummary } from './player-summary.model';

@Component({
  selector: 'app-player-summary',
  templateUrl: './player-summary.component.html',
  styleUrls: ['./player-summary.component.scss'],
})
export class PlayerSummaryComponent implements OnInit {
  playerSummary: PlayerSummary | null = null;
  playerId: number = 1;
  lastAttemptedPlayerId: number | null = null;
  playerNotFound: boolean = false;

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    this.loadPlayer();
  }

  loadPlayer(): void {
    this.lastAttemptedPlayerId = this.playerId;
    this.fetchPlayerSummary(this.playerId);
  }

  fetchPlayerSummary(playerID: number): void {
    this.http
      .get<PlayerSummary>(
        `http://localhost:8000/api/v1/playerSummary/${playerID}`
      )
      .subscribe(
        (data) => {
          if (data && Object.keys(data).length > 0) {
            this.playerSummary = data;
            this.playerNotFound = false;
          } else {
            this.playerSummary = null;
            this.playerNotFound = true;
          }
        },
        (error) => {
          this.playerSummary = null;
          this.playerNotFound = true;
        }
      );
  }
}
