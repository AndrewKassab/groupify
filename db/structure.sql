SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: ar_internal_metadata; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ar_internal_metadata (
    key character varying NOT NULL,
    value character varying,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL
);


--
-- Name: genres; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.genres (
    id bigint NOT NULL,
    name character varying,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL
);


--
-- Name: genres_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.genres_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: genres_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.genres_id_seq OWNED BY public.genres.id;


--
-- Name: group_spotify_accounts; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.group_spotify_accounts (
    id bigint NOT NULL,
    group_id integer NOT NULL,
    spotify_account_id integer NOT NULL
);


--
-- Name: group_spotify_accounts_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.group_spotify_accounts_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: group_spotify_accounts_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.group_spotify_accounts_id_seq OWNED BY public.group_spotify_accounts.id;


--
-- Name: groups; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.groups (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    title character varying NOT NULL,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL
);


--
-- Name: groups_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.groups_id_seq OWNED BY public.groups.id;


--
-- Name: schema_migrations; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.schema_migrations (
    version character varying NOT NULL
);


--
-- Name: spotify_accounts; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.spotify_accounts (
    id bigint NOT NULL,
    user_id integer,
    username character varying NOT NULL,
    spotify_id character varying NOT NULL,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL
);


--
-- Name: spotify_accounts_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.spotify_accounts_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: spotify_accounts_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.spotify_accounts_id_seq OWNED BY public.spotify_accounts.id;


--
-- Name: spotify_playlists; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.spotify_playlists (
    id bigint NOT NULL,
    group_id integer NOT NULL,
    user_id integer NOT NULL,
    spotify_id character varying,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL
);


--
-- Name: spotify_playlists_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.spotify_playlists_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: spotify_playlists_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.spotify_playlists_id_seq OWNED BY public.spotify_playlists.id;


--
-- Name: track_genres; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.track_genres (
    id bigint NOT NULL,
    track_id integer NOT NULL,
    genre_id integer NOT NULL
);


--
-- Name: track_genres_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.track_genres_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: track_genres_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.track_genres_id_seq OWNED BY public.track_genres.id;


--
-- Name: tracks; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.tracks (
    id bigint NOT NULL,
    name character varying,
    duration integer,
    spotify_id character varying,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL,
    group_id integer,
    rank integer,
    artists character varying
);


--
-- Name: tracks_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.tracks_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: tracks_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.tracks_id_seq OWNED BY public.tracks.id;


--
-- Name: user_genres; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.user_genres (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    genre_id integer NOT NULL
);


--
-- Name: user_genres_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.user_genres_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: user_genres_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.user_genres_id_seq OWNED BY public.user_genres.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.users (
    id bigint NOT NULL,
    email character varying NOT NULL,
    name character varying NOT NULL,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL
);


--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.users_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: genres id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.genres ALTER COLUMN id SET DEFAULT nextval('public.genres_id_seq'::regclass);


--
-- Name: group_spotify_accounts id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.group_spotify_accounts ALTER COLUMN id SET DEFAULT nextval('public.group_spotify_accounts_id_seq'::regclass);


--
-- Name: groups id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.groups ALTER COLUMN id SET DEFAULT nextval('public.groups_id_seq'::regclass);


--
-- Name: spotify_accounts id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.spotify_accounts ALTER COLUMN id SET DEFAULT nextval('public.spotify_accounts_id_seq'::regclass);


--
-- Name: spotify_playlists id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.spotify_playlists ALTER COLUMN id SET DEFAULT nextval('public.spotify_playlists_id_seq'::regclass);


--
-- Name: track_genres id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.track_genres ALTER COLUMN id SET DEFAULT nextval('public.track_genres_id_seq'::regclass);


--
-- Name: tracks id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.tracks ALTER COLUMN id SET DEFAULT nextval('public.tracks_id_seq'::regclass);


--
-- Name: user_genres id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.user_genres ALTER COLUMN id SET DEFAULT nextval('public.user_genres_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Name: ar_internal_metadata ar_internal_metadata_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ar_internal_metadata
    ADD CONSTRAINT ar_internal_metadata_pkey PRIMARY KEY (key);


--
-- Name: genres genres_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.genres
    ADD CONSTRAINT genres_pkey PRIMARY KEY (id);


--
-- Name: group_spotify_accounts group_spotify_accounts_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.group_spotify_accounts
    ADD CONSTRAINT group_spotify_accounts_pkey PRIMARY KEY (id);


--
-- Name: groups groups_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.groups
    ADD CONSTRAINT groups_pkey PRIMARY KEY (id);


--
-- Name: schema_migrations schema_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.schema_migrations
    ADD CONSTRAINT schema_migrations_pkey PRIMARY KEY (version);


--
-- Name: spotify_accounts spotify_accounts_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.spotify_accounts
    ADD CONSTRAINT spotify_accounts_pkey PRIMARY KEY (id);


--
-- Name: spotify_playlists spotify_playlists_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.spotify_playlists
    ADD CONSTRAINT spotify_playlists_pkey PRIMARY KEY (id);


--
-- Name: track_genres track_genres_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.track_genres
    ADD CONSTRAINT track_genres_pkey PRIMARY KEY (id);


--
-- Name: tracks tracks_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.tracks
    ADD CONSTRAINT tracks_pkey PRIMARY KEY (id);


--
-- Name: user_genres user_genres_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.user_genres
    ADD CONSTRAINT user_genres_pkey PRIMARY KEY (id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: index_genres_on_name; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX index_genres_on_name ON public.genres USING btree (name);


--
-- Name: index_group_spotify_accounts_on_group_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX index_group_spotify_accounts_on_group_id ON public.group_spotify_accounts USING btree (group_id);


--
-- Name: index_group_spotify_accounts_on_spotify_account_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX index_group_spotify_accounts_on_spotify_account_id ON public.group_spotify_accounts USING btree (spotify_account_id);


--
-- Name: index_groups_on_user_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX index_groups_on_user_id ON public.groups USING btree (user_id);


--
-- Name: index_spotify_accounts_on_spotify_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX index_spotify_accounts_on_spotify_id ON public.spotify_accounts USING btree (spotify_id);


--
-- Name: index_spotify_accounts_on_user_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX index_spotify_accounts_on_user_id ON public.spotify_accounts USING btree (user_id);


--
-- Name: index_spotify_accounts_on_username; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX index_spotify_accounts_on_username ON public.spotify_accounts USING btree (username);


--
-- Name: index_spotify_playlists_on_group_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX index_spotify_playlists_on_group_id ON public.spotify_playlists USING btree (group_id);


--
-- Name: index_spotify_playlists_on_user_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX index_spotify_playlists_on_user_id ON public.spotify_playlists USING btree (user_id);


--
-- Name: index_track_genres_on_genre_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX index_track_genres_on_genre_id ON public.track_genres USING btree (genre_id);


--
-- Name: index_track_genres_on_track_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX index_track_genres_on_track_id ON public.track_genres USING btree (track_id);


--
-- Name: index_tracks_on_name; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX index_tracks_on_name ON public.tracks USING btree (name);


--
-- Name: index_tracks_on_spotify_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX index_tracks_on_spotify_id ON public.tracks USING btree (spotify_id);


--
-- Name: index_user_genres_on_genre_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX index_user_genres_on_genre_id ON public.user_genres USING btree (genre_id);


--
-- Name: index_user_genres_on_user_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX index_user_genres_on_user_id ON public.user_genres USING btree (user_id);


--
-- Name: group_spotify_accounts fk_rails_02ab1618d8; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.group_spotify_accounts
    ADD CONSTRAINT fk_rails_02ab1618d8 FOREIGN KEY (spotify_account_id) REFERENCES public.spotify_accounts(id);


--
-- Name: track_genres fk_rails_5ca60a330d; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.track_genres
    ADD CONSTRAINT fk_rails_5ca60a330d FOREIGN KEY (genre_id) REFERENCES public.genres(id);


--
-- Name: groups fk_rails_5e78cd340a; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.groups
    ADD CONSTRAINT fk_rails_5e78cd340a FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- Name: spotify_playlists fk_rails_7241dcf17c; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.spotify_playlists
    ADD CONSTRAINT fk_rails_7241dcf17c FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- Name: group_spotify_accounts fk_rails_804114d80e; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.group_spotify_accounts
    ADD CONSTRAINT fk_rails_804114d80e FOREIGN KEY (group_id) REFERENCES public.groups(id);


--
-- Name: user_genres fk_rails_891e09a06e; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.user_genres
    ADD CONSTRAINT fk_rails_891e09a06e FOREIGN KEY (genre_id) REFERENCES public.genres(id);


--
-- Name: track_genres fk_rails_968410268d; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.track_genres
    ADD CONSTRAINT fk_rails_968410268d FOREIGN KEY (track_id) REFERENCES public.tracks(id);


--
-- Name: user_genres fk_rails_b570792877; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.user_genres
    ADD CONSTRAINT fk_rails_b570792877 FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- Name: spotify_playlists fk_rails_bd6209a3bc; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.spotify_playlists
    ADD CONSTRAINT fk_rails_bd6209a3bc FOREIGN KEY (group_id) REFERENCES public.groups(id);


--
-- Name: spotify_accounts fk_rails_f2f39d3641; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.spotify_accounts
    ADD CONSTRAINT fk_rails_f2f39d3641 FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- PostgreSQL database dump complete
--

SET search_path TO "$user", public;

INSERT INTO "schema_migrations" (version) VALUES
('20190425233315'),
('20190503000150'),
('20190504085846'),
('20190506201347');


